# -*- coding: utf-8 -*-

import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from ibanmanager.bank import models as bank_models
from ibanmanager.bank import serializers as bank_serializers
from ibanmanager.users import models as user_models

class AccountFilter(django_filters.FilterSet):

    from_date = django_filters.IsoDateTimeFilter(field_name="created_at", lookup_expr='gte')
    to_date = django_filters.IsoDateTimeFilter(field_name="created_at", lookup_expr='lte')


    class Meta:
        model = bank_models.Account
        fields = '__all__'


class AccountPermission(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        is_authenticated = super(AccountPermission, self).has_permission(request, view)
        return is_authenticated and request.user.type == user_models.USER_TYPE.ADMIN

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.owner.created_by == request.user


class AccountViewSet(ModelViewSet):

    queryset = bank_models.Account.objects.all()
    serializer_class = bank_serializers.AccountSerializer
    permission_classes = (AccountPermission,)

    filter_class = AccountFilter
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    ordering_fields = '__all__'

    def get_queryset(self):
        queryset = super(AccountViewSet, self).get_queryset()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset
