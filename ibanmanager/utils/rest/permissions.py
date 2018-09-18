from rest_framework import permissions
from django.conf import settings
from thearomatrace.users import models as user_models


class CustomIsAdminUser(permissions.IsAdminUser):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated() and request.user.is_staff and request.user.type == user_models.UserType.ADMIN



class IsStaffUser(CustomIsAdminUser):

    def has_permission(self, request, view):
        if settings.DEBUG:
            return True
        else:
            return super(IsStaffUser,self).has_permission(request, view)

