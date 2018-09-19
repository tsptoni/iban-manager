# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from ibanmanager.utils.models.base import BaseModel
from ibanmanager.utils.enum import DumbEnum

import uuid


UserType = DumbEnum(
        ("INDIVIDUAL", _("Individual")),
        ("ADMIN", _("Admin"))
    )

class User(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)

    AbstractUser.REQUIRED_FIELDS += ('type',)

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
                                        type=UserType.ADMIN)


        pwd = cls.objects.make_random_password() if password == None else password
        new_user.set_password(pwd)
        new_user.save()

        return (new_user, pwd)
