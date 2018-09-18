# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework import routers

from . import views_api as user_views_api
from . import views as user_views
from django.conf.urls import url, include

router = routers.DefaultRouter()
router.register(r'user', user_views_api.UserViewSet)


urlpatterns = [
    url(r'^login/', user_views_api.ObtainAuthTokenAndUser.as_view(), name='obtain_auth_token_and_user'),
    url(r'^logout/', user_views_api.CustomLogoutView.as_view(), name='logout'),
    url(r'^register/$', user_views_api.CustomRegistration.as_view(), name='register'),
    url(r'^', include(router.urls)),
    url(r'^password/reset/$', user_views_api.TokenCreateResetPasswordView.as_view(), name='password_reset'),
    url(r'^password/new/(?P<token>[\w]{40})/$', user_views.password_new, name='password_new'),
]



