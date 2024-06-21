from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import UserTI
from .forms import CustomUserCreationForm

class UserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm

    list_display = ('email', 'is_active', 'is_staff', 'created_at')
    list_filter = ('is_active', 'is_staff')
    search_fields = ('email',)

    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (('Личные данные'), {'fields': ('username', 'avatar')}),
        (('Разрешения'), {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
        (('Важные даты'), {'fields': ('created_at', 'updated_at')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    
admin.site.register(UserTI, UserAdmin)