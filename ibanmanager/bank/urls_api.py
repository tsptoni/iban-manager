# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.urls import path, include
from rest_framework import routers

from . import views_api

router = routers.DefaultRouter()
router.register(r'account', views_api.AccountViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

