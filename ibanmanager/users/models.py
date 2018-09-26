# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from ibanmanager.utils.enum import DumbEnum
from ibanmanager.utils.models.fields import FirstUserField

import uuid


USER_TYPE = DumbEnum(
        ("INDIVIDUAL", _("Individual")),
        ("ADMIN", _("Admin"))
    )

class User(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    type = models.CharField(max_length=20, choices=USER_TYPE, default=USER_TYPE.INDIVIDUAL)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=90)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = FirstUserField(blank=True, null=True, on_delete=models.SET_NULL)

    AbstractUser.REQUIRED_FIELDS += ('type', 'first_name', 'last_name')

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

    @classmethod
    def create_admin_user(cls, email, first_name=None, last_name=None, password=None):
        new_user = cls.objects.create(username=email,
                                        first_name=first_name,
                                        last_name=last_name,
                                        email=email,
                                        is_staff=True,
                                        is_superuser=True,
                                        is_active=True,
                                        type=USER_TYPE.ADMIN)


        pwd = cls.objects.make_random_password() if password == None else password
        new_user.set_password(pwd)
        new_user.save()

        return (new_user, pwd)

    class Meta:
        ordering = ('-modified_at',)