from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from api.models import User
# Register your models here.
class UserAdmin(AuthUserAdmin):
    list_display = AuthUserAdmin.list_display + ('role',)
    fieldsets = AuthUserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )
    add_fieldsets = AuthUserAdmin.add_fieldsets + (
        (None, {'fields': ('role',)}),
    )

admin.site.register(User, UserAdmin)
