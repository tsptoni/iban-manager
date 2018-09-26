from django.db.models import signals
from django.utils.functional import curry
from django.utils.decorators import decorator_from_middleware
from django.utils.deprecation import MiddlewareMixin
from oauth2_provider.models import AccessToken

from ibanmanager.utils.models.fields import FirstRegistry, LastRegistry


class FirstUserMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.method == 'POST':
            if request.user and request.user.is_authenticated:
                user = request.user
            else:
                user = None

            update_users = curry(self.update_users, user)
            signals.pre_save.connect(update_users, dispatch_uid=request, weak=False)

    def update_users(self, user, sender, instance, **kwargs):
        registry = FirstRegistry()
        if sender in registry:
            for field in registry.get_fields(sender):
                setattr(instance, field.name, user)

    def process_response(self, request, response):
        signals.pre_save.disconnect(dispatch_uid=request)
        return response

record_first_current_user = decorator_from_middleware(FirstUserMiddleware)


class LastUserMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.method in ['PUT', 'PATCH']:
            if request.user and request.user.is_authenticated:
                user = request.user
            else:
                user = None

            update_users = curry(self.update_users, user)
            signals.pre_save.connect(update_users, dispatch_uid=request, weak=False)

    def update_users(self, user, sender, instance, **kwargs):
        registry = LastRegistry()
        if sender in registry:
            for field in registry.get_fields(sender):
                setattr(instance, field.name, user)

    def process_response(self, request, response):
        signals.pre_save.disconnect(dispatch_uid=request)
        return response

record_last_current_user = decorator_from_middleware(LastUserMiddleware)