
from django.utils.deprecation import MiddlewareMixin
from oauth2_provider.models import AccessToken


class AuthenticationMiddlewareJWT(MiddlewareMixin):

    def process_request(self, request):
        if not request.user or not request.user.is_authenticated:
            try:
                bearer = request.META.get('HTTP_AUTHORIZATION', None)
                bearer = bearer.split()[-1]
                access_token = AccessToken.objects.filter(token=bearer).first()
                if access_token:
                    user = access_token.user
                    request.user = user
            except Exception as e:
                pass
