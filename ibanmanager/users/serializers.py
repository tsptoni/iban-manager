# -*- coding: utf-8 -*-

from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers, exceptions
from rest_framework.authtoken.serializers import AuthTokenSerializer

from djoser.serializers import UserRegistrationSerializer

from ibanmanager.users import models


class ExtendedAuthTokenSerializer(AuthTokenSerializer):

    def validate(self, attrs):
        super(ExtendedAuthTokenSerializer, self).validate(attrs)

        username = attrs.get('username')
        password = attrs.get('password')
        user = None

        if username and password:
            user = authenticate(username=username, password=password)

            if user:
                if not user.is_active:
                    msg = _('User account is disabled.')
                    raise serializers.ValidationError(msg)
            else:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg)
        else:
            msg = _('"username" and "password" fields are mandatory.')
            raise serializers.ValidationError(msg)

        attrs['user'] = user
        return attrs


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


class ExtendedUserRegistrationSerializer(UserRegistrationSerializer):

    def create(self, validated_data):

        user_type = validated_data.get('type', None)
        if user_type == models.UserType.ADMIN:
            validated_data['is_staff'] = True
        else:
            validated_data['is_staff'] = False

        user = models.User.objects.create_user(**validated_data)

        return user

    def validate_email(self, value):
        if value is None or value == '':
            raise serializers.ValidationError(_('This field cannot be blank.'))

        return value


    class Meta:
        model = models.User
        fields = UserRegistrationSerializer.Meta.fields + ('first_name', 'last_name', 'is_superuser')


class TokenResetPasswordSerializer(serializers.ModelSerializer):

    use = serializers.SerializerMethodField(read_only=True)
    token = serializers.SerializerMethodField(read_only=True)

    @staticmethod
    def setup_eager_loading(queryset):
        return queryset

