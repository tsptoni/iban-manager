# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver

import rest_framework.authtoken.models

from ibanmanager.utils.models.base import BaseModel
from ibanmanager.utils.enum import DumbEnum

import uuid


UserType = DumbEnum(
        ("INDIVIDUAL", _("Individual")),
        ("ADMIN", _("Admin"))
    )

class User(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)

    AbstractUser.REQUIRED_FIELDS += ('type',)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

    @classmethod
    def create_admin_user(cls, email, first_name=None, last_name=None, password=None):
        new_user = cls.objects.create(username=email,
                                        first_name=first_name,
                                        last_name=last_name,
                                        email=email,
                                        is_staff=True,
                                        is_superuser=True,
                                        is_active=True,
                                        type=UserType.ADMIN)


        pwd = cls.objects.make_random_password() if password == None else password
        new_user.set_password(pwd)
        new_user.save()

        return (new_user, pwd)


@python_2_unicode_compatible
class Token(rest_framework.authtoken.models.Token):
    # key is no longer primary key, but still indexed and unique
    key = models.CharField(_("Key"), max_length=40, db_index=True, unique=True)
    # relation to user is a ForeignKey, so each user can have more than one token
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='auth_tokens',
        on_delete=models.CASCADE, verbose_name=_("User")
    )


class TokenResetPassword(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    token = models.CharField(max_length=40, db_index=True, unique=True)


@receiver(post_save, sender=TokenResetPassword)
def post_save_tokenresetpassword(sender, instance, created, **kwargs):

    email = instance.user.email
    token = instance.token

    subject = 'Reset Password'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]
    email_context_data = {
        'username': instance.user.username,
        'token': instance.token
    }

    msg_plain = render_to_string('users/mailings/reset_password.txt', email_context_data)
    msg_html = render_to_string('users/mailings/reset_password.html', email_context_data)

    send_mail(subject,
              msg_plain,
              from_email,
              recipient_list,
              fail_silently=False,
              html_message=msg_html)

