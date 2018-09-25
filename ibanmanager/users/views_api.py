# -*- coding: utf-8 -*-

from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from ibanmanager.users import serializers as user_serializers
from ibanmanager.users import models as user_models


class UserCustomPermission(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        is_authenticated = super(UserCustomPermission, self).has_permission(request, view)
        return is_authenticated and request.user.type == user_models.USER_TYPE.ADMIN

    def has_object_permission(self, request, view, obj):
        print(request.data)
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.created_by == request.user


class UserViewSet(ModelViewSet):

    serializer_class = user_serializers.UserSerializer
    filter_fields = ('type',)

    queryset = user_models.User.objects.all()
    permission_classes = (UserCustomPermission,)

    def get_queryset(self):
        result = user_models.User.objects.filter(type=user_models.USER_TYPE.INDIVIDUAL)

        return user_serializers.UserSerializer.setup_eager_loading(result)


    def get_serializer_context(self):
        context = {}
        return context

