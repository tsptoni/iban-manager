from django.contrib import admin
from ibanmanager.bank import models as bank_models

class AccountAdmin(admin.ModelAdmin):

    list_display = ('id', 'owner', 'iban', )
    list_display_links = ('id',)
    search_fields = ('name', 'owner__username', 'owner__email', 'iban',)
    list_filter = ('owner', 'created_by')


admin.site.register(bank_models.Account, AccountAdmin)