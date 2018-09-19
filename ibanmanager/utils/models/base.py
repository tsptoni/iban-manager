# -*- coding: utf-8 -*-

from django.db import models
import uuid

class BaseModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('-modified_at',)