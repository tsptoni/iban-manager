# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import

from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save
from django.dispatch import receiver

from ibanmanager.utils.models.base import BaseModel
from ibanmanager.utils.models.validators import validate_iban

from stdnum import iban


class Account(BaseModel):

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='accounts')
    iban = models.CharField(max_length=45, validators=[validate_iban])

    def __str__(self):
        return self.iban


@receiver(pre_save, sender=Account)
def pre_save_account(sender, instance, **kwargs):

    instance.iban = iban.format(instance.iban)