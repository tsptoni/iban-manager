from datetime import datetime, timedelta

import pytz
from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication
from django.utils.translation import ugettext_lazy as _
from ibanmanager.users.models import Token

class ExpiringTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        # model = self.get_model()
        model = Token
        try:
            token = model.objects.select_related('user').get(key=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed(_('Invalid token'))

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed(_('User inactive or deleted'))

        # This is required for the time comparison
        utc_now = datetime.utcnow()
        utc_now = utc_now.replace(tzinfo=pytz.utc)

        if token.created < utc_now - timedelta(days=30):
            raise exceptions.AuthenticationFailed(_('Token has expired'))

        return token.user, token