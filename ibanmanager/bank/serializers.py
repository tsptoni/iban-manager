# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import PermissionDenied
from rest_framework import serializers

from ibanmanager.bank import models as bank_models

class AccountSerializer(serializers.ModelSerializer):


    @staticmethod
    def setup_eager_loading(queryset):

        queryset = queryset.select_related('owner')

        return queryset

    def validate(self, attrs):
        user = self.context.get('request').user
        if not self.instance:
            owner = attrs.get('owner', None)
            if owner.created_by != user:
                raise PermissionDenied(_("Forbidden."))

        return super(AccountSerializer, self).validate(attrs)


    class Meta:
        model = bank_models.Account
        fields = '__all__'