# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [

        url(r'^admin/', include(admin.site.urls)),
        url(r'^api/v1/users/', include('ibanmanager.users.urls_api', namespace='api-v1-users')),
        url(r'^api/v1/bank/', include('ibanmanager.bank.urls_api', namespace='api-v1-bank')),

] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

