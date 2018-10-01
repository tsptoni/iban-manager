from django.core.management.base import BaseCommand
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from ibanmanager.users import models as user_models

class Command(BaseCommand):
    help = _('Creates the first ADMIN users. Usage: create_first_admin_user')

    def add_arguments(self, parser):
        parser.add_argument('args', nargs='*')

    def handle(self, *args, **options):

        admin_emails = settings.FIRST_ADMIN_USERS
        print('emails: ', admin_emails)

        for email in admin_emails:

            first_name, last_name = email.split('@')

            if user_models.User.objects.filter(email=email).exists():
                self.stdout.write(self.style.ERROR(_('Skipping {} because already exists.'.format(email))))
            else:
                (new_user, raw_password) = user_models.User.create_admin_user(email=email, first_name=first_name, last_name=last_name)

                self.stdout.write(self.style.SUCCESS(
                    _('Created successfully ADMIN user with Email: {} | Password: {}').format(
                        new_user.username, raw_password))
                )
