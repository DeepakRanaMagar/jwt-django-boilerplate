from django.contrib import admin

from .models import Accounts


@admin.register(Accounts)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'address', 'phone_no', 'is_admin', 'created_at', 'modified_at']