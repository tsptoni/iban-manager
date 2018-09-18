# -*- coding: utf-8 -*-

from .enum import DumbEnum
from django.utils.translation import ugettext_lazy as _

SupportedLanguages = DumbEnum(
        ('en', _('English')),
        ('es', _('Spanish')),
        ('es', _('Spanish')),
        ('pt', _('Portuguese')),
        ('it', _('Italian')),
        ('de', _('German')),
        ('fr', _('French')),
        ('nl', _('Dutch')),
    )