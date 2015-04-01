from django.contrib import admin
from .models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'is_admin', 'is_mod')
admin.site.register(Account, AccountAdmin)
