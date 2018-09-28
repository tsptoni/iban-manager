# -*- coding: utf-8 -*-

from rest_framework import serializers
from ibanmanager.users import models
from ibanmanager.bank import serializers as bank_serializers


class UserLiteSerializer(serializers.ModelSerializer):

    @staticmethod
    def setup_eager_loading(queryset):

        return queryset

    class Meta:
        model = models.User
        fields = ('id', 'username', 'email', 'type', 'created_by')
        read_only_fields = ('id', 'username', 'email', 'type',)


class UserSerializer(serializers.ModelSerializer):

    accounts = bank_serializers.AccountSerializer(many=True, read_only=True)
    created_by = serializers.CharField(source='created_by.username', read_only=True)

    @staticmethod
    def setup_eager_loading(queryset):

        return queryset


    class Meta:
        model = models.User
        fields = ('id','first_name', 'last_name', 'email', 'last_login', 'username', 'is_active', 'type',
                  'is_superuser', 'accounts', 'created_at', 'modified_at', 'created_by')
        read_only_fields = ('id', 'last_login', 'is_active', 'type', 'is_superuser')