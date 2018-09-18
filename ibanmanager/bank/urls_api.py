# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.conf.urls import url, include
from rest_framework import routers

from . import views_api

router = routers.DefaultRouter()

urlpatterns = [
    url(r'', include(router.urls)),
]

