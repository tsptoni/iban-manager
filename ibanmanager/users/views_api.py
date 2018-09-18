# -*- coding: utf-8 -*-


from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now as timezone_now
from django.shortcuts import get_object_or_404
from django.db import IntegrityError
from django.db import transaction

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import DestroyAPIView
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework import mixins as rf_mixins, filters
from rest_framework import permissions
from rest_framework import status

from datetime import datetime, timedelta

from ibanmanager.users.serializers import ExtendedAuthTokenSerializer, ExtendedUserRegistrationSerializer
from ibanmanager.users import serializers as user_serializers
from ibanmanager.users import models as user_models
from ibanmanager.utils.rest.mixins import PartialUpdateModelMixin

import djoser.views
import hashlib
import random
import pytz
import time

class ObtainAuthTokenAndUser(ObtainAuthToken):
    serializer_class = ExtendedAuthTokenSerializer


    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        data = {}

        if user is not None:

            if not user.is_active:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data={'email': [_('Email address not verified yet.')]})

            else:
                utc_old = datetime.utcnow()
                utc_old = utc_old.replace(tzinfo=pytz.utc) - timedelta(days=30)
                user_models.Token.objects.filter(user=user, created__lte=utc_old)

                try:
                    # token = Token.objects.create(user=user)
                    token = user_models.Token.objects.create(user=user)
                except IntegrityError:
                    return Response(status=status.HTTP_409_CONFLICT,
                                    data={'non_field_error': [
                                            _('Conflict: Multiple GetToken Requests run in parallel.')]})

                user.last_login = timezone_now()

                user.save()

            token_response = Response({'token': token.key})

            data = {
                'token': token_response.data['token'],
                'user_id': user.id,
                'type': user.type,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'is_superuser': user.is_superuser
            }

        return Response(data)


class CustomActivationView(djoser.views.ActivationView):
    @transaction.atomic
    def post(self, request):
        response = super(CustomActivationView, self).post(request)

        if response.status_code == status.HTTP_400_BAD_REQUEST:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=response)
        else:
            return response


class CustomLogoutView(djoser.views.LogoutView):
    @transaction.atomic
    def post(self, request):
        response = super(CustomLogoutView, self).post(request)

        if response.status_code == status.HTTP_400_BAD_REQUEST:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=response)
        else:
            return response


class RegistrationCustomPermission(permissions.IsAuthenticated):

    def has_permission(self, request, view):
        is_authenticated = super(RegistrationCustomPermission, self).has_permission(request, view)

        if not is_authenticated and (not 'type' in request.data or request.data['type'] == user_models.UserType.INDIVIDUAL):
            return True

        if is_authenticated and request.user.type == user_models.UserType.ADMIN:
            return True

        return False


class UnregistrationCustomPermission(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        if obj.is_superuser:
            if obj.type == user_models.UserType.ADMIN:
                return False #Not possible to remove a ADMIN superuser
            else:
                return request.user.type == user_models.UserType.ADMIN #Only ADMINs can remove other type superusers
        else:
            if request.user.type == user_models.UserType.ADMIN:
                return True
            else:
                return False


class CustomRegistration(djoser.views.RegistrationView):
    serializer_class = ExtendedUserRegistrationSerializer
    permission_classes = (RegistrationCustomPermission,)

    def get_email_context(self, user):
        context = super(CustomRegistration, self).get_email_context(user)
        context['username'] = user.username
        context['password'] = self.request.data['password']
        return context


class UnregisterUserView(DestroyAPIView):
    queryset = user_models.User.objects.all()
    permission_classes = (UnregistrationCustomPermission,)


class UserCustomPermission(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        is_authenticated = super(UserCustomPermission, self).has_permission(request, view)

        if not is_authenticated:
            return False
        else:
            return request.user.type == user_models.UserType.ADMIN

    def has_object_permission(self, request, view, obj):
        if request.user.type == user_models.UserType.ADMIN:
            return True
        else:
            # return obj.id == request.user.id #Other users can only
            return False


class UserViewSet(rf_mixins.RetrieveModelMixin,
                  PartialUpdateModelMixin,
                  rf_mixins.ListModelMixin,
                  GenericViewSet):

    serializer_class = user_serializers.UserSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('type', 'is_superuser')

    queryset = user_models.User.objects.all()
    permission_classes = (UserCustomPermission,)

    def get_queryset(self):
        result = user_models.User.objects.all()

        if self.request.query_params.get('is_superuser', None) != None:
            filter_is_superuser = self.request.query_params.get('is_superuser', 'false').lower() == 'true'
            result = result.filter(is_superuser=filter_is_superuser)

        return user_serializers.UserSerializer.setup_eager_loading(result)


    def get_serializer_context(self):
        context = {
        }
        return context

class TokenCreateResetPasswordView(APIView):

    def post(self, request, format=None):

        email = request.data['email']
        timestamp = time.time()
        float_random = random.uniform(0, 100)

        seed = '{0}{1}'.format(timestamp, float_random)
        token = hashlib.sha1(seed.encode('utf-8')).hexdigest()

        user = user_models.User.objects.filter(email=email).first()

        if user:
            user_models.TokenResetPassword.objects.create(user=user, token=token)

        data = {
            'status': 'OK'
        }
        return Response(data=data, status=status.HTTP_200_OK)


