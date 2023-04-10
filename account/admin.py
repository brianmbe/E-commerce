from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Register your models here.


@admin.register(Account)
class AccountAdmin(UserAdmin):
    list_display = ['email', 'first_name', 'last_name',
                    'username', 'last_login', 'date_joined', 'is_active', 'is_admin', 'is_superadmin']
    list_filter = ['email', 'first_name', 'last_name']
    search_fields = ['first_name', 'last_name']
    list_display_links = ['email', 'first_name']
    readonly_fields = ['last_login', 'date_joined']
    ordering = ['-date_joined']
    filter_horizontal = []
    filter_vertical = []
    fieldsets = []
