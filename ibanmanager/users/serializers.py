# -*- coding: utf-8 -*-

from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
from ibanmanager.users import models


class UserSerializer(serializers.ModelSerializer):

    @staticmethod
    def setup_eager_loading(queryset):

        return queryset


    class Meta:
        model = models.User
        fields = ('id','first_name', 'last_name', 'email', 'last_login', 'username', 'is_active', 'type', 'is_superuser',)
        read_only_fields = ('id', 'last_login', 'username', 'email', 'is_active', 'type', 'is_superuser')



class UserLiteSerializer(serializers.ModelSerializer):

    @staticmethod
    def setup_eager_loading(queryset):

        return queryset

    class Meta:
        model = models.User
        fields = ('id', 'username', 'email', 'type')
        read_only_fields = ('id', 'username', 'email', 'type',)

