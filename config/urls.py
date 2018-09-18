# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

        url(r'^admin/', include(admin.site.urls)),
        url(r'^api/v1/users/', include('ibanmanager.users.urls_api', namespace='api-v1-users')),
        url(r'^api/v1/bank/', include('ibanmanager.bank.urls_api', namespace='api-v1-bank')),

]

