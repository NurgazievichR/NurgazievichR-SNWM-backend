from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserTI


admin.site.register(UserTI)