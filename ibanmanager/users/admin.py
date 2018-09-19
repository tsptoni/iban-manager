from django.contrib import admin
from ibanmanager.users import models as user_models
from ibanmanager.bank import models as bank_models

class AccountStackedInline(admin.StackedInline):
    model = bank_models.Account
    max_num = 0
    fk_name = 'owner'
    readonly_fields = ('id', 'owner', 'iban', 'created_by')


class UserAdmin(admin.ModelAdmin):

    list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'type')
    list_display_links = ('id', 'username',)
    search_fields = ('name', 'username', 'first_name', 'last_name', 'email')
    list_filter = ('type', 'created_by')

    inlines = [AccountStackedInline]


admin.site.register(user_models.User, UserAdmin)