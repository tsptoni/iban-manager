# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin


urlpatterns = [
        path('admin/',  admin.site.urls),
        path('api/v1/users/', include('ibanmanager.users.urls_api')),
        path('api/v1/bank/', include('ibanmanager.bank.urls_api')),
        path('auth/', include('rest_framework_social_oauth2.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)