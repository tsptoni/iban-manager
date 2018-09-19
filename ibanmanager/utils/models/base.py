# -*- coding: utf-8 -*-

from django.db import models

from ibanmanager.utils.models.fields import FirstUserField

import uuid



class BaseModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = FirstUserField(blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        abstract = True
        ordering = ('-modified_at',)