from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts import models as account_models

class AccountAdmin(UserAdmin):
    list_display = ('username',
                    'email')
    search_fields = ('username', 'email')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(account_models.Account, AccountAdmin)
