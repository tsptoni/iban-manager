# -*- coding: utf-8 -*-

from rest_framework import serializers

from ibanmanager.bank import models as bank_models

class AccountSerializer(serializers.ModelSerializer):


    @staticmethod
    def setup_eager_loading(queryset):

        queryset = queryset.select_related('owner')

        return queryset


    class Meta:
        model = bank_models.Account