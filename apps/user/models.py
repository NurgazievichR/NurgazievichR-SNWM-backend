from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from apps.user.managers import CustomManager

class UserTI(AbstractBaseUser, PermissionsMixin):
    last_login = None
    is_superuser = None

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, blank=True, default="")
    avatar = models.ImageField(upload_to='users_avatars', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)

    objects = CustomManager()

    def __str__(self) -> str:
        return f"Email: {self.email}"
    
    def has_perm(self, perm, obj=None):
        return self.is_active and self.is_staff
    
    def has_module_perms(self, app_label):
        return self.is_active and self.is_staff
    
    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
