# -*- coding: utf-8 -*-

from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins as rf_mixins
from rest_framework import permissions
from ibanmanager.users import serializers as user_serializers
from ibanmanager.users import models as user_models
from ibanmanager.utils.rest.mixins import PartialUpdateModelMixin


class UserCustomPermission(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        is_authenticated = super(UserCustomPermission, self).has_permission(request, view)
        return is_authenticated and request.user.type == user_models.USER_TYPE.ADMIN

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.created_by.pk == request.user.pk


class UserViewSet(rf_mixins.RetrieveModelMixin,
                  PartialUpdateModelMixin,
                  rf_mixins.ListModelMixin,
                  GenericViewSet):

    serializer_class = user_serializers.UserSerializer
    filter_fields = ('type', 'is_superuser')

    queryset = user_models.User.objects.all()
    permission_classes = (UserCustomPermission,)

    def get_queryset(self):
        result = user_models.User.objects.filter(type=user_models.USER_TYPE.INDIVIDUAL)

        if self.request.query_params.get('is_superuser', None) != None:
            filter_is_superuser = self.request.query_params.get('is_superuser', 'false').lower() == 'true'
            result = result.filter(is_superuser=filter_is_superuser)

        return user_serializers.UserSerializer.setup_eager_loading(result)


    def get_serializer_context(self):
        context = {
        }
        return context

