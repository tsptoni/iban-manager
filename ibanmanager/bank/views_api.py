# -*- coding: utf-8 -*-

import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers as rf_serializers


from ibanmanager.bank import models as bank_models
from ibanmanager.bank import serializers as bank_serializers

class AccountFilter(django_filters.FilterSet):

    from_date = django_filters.IsoDateTimeFilter(name="created_at", lookup_expr='gte')
    to_date = django_filters.IsoDateTimeFilter(name="created_at", lookup_expr='lte')


    def get_name(self, name, value):
        qs = self.filter(name__unaccent__icontains=value).order_by(name) # .order_by(Length(name).asc())
        return qs

    name = django_filters.CharFilter(method=get_name)


    class Meta:
        model = bank_models.Account
        fields = '__all__'
        exclude = ('location',)



class AccountViewSet(ModelViewSet):

    queryset = bank_models.Account.objects.all()
    serializer_class = bank_serializers.AccountSerializer

    filter_class = AccountFilter
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    ordering_fields = '__all__'

    def get_queryset(self):
        queryset = super(AccountViewSet, self).get_queryset()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset
