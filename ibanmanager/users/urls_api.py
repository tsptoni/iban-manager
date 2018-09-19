# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework import routers

from . import views_api as user_views_api
from . import views as user_views
from django.conf.urls import url, include

router = routers.DefaultRouter()
router.register(r'user', user_views_api.UserViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]



