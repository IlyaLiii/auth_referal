from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from .scripts import generate_invite_code

LENGTH_INVITE_CODE = 6

class User(AbstractBaseUser):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        max_length=150,
        unique=True,
    )
    phone_number = models.CharField(
        max_length=12,
        null=False,
    )
    invite_code = models.CharField(
        max_length=6,
        null=False,
    )
    inviting_user = models.CharField(
        max_length=6,
        blank=True,
        null=True,
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    def create_user(self, username, phone_number, invite_code, invite_user, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(
           username, phone_number, invite_code, invite_user, password, **extra_fields
        )
    
    def save(self, *args, **kwargs):
        if not self.invite_code:
            self.invite_code = generate_invite_code(LENGTH_INVITE_CODE)
        super().save(*args, **kwargs)

    def update_inviting_code(self, inviting_user, invite_code):
        select_user = User.objects.get(inviting_user=self.invite_code)
        select_user.inviting_code = self.invite_code
        
        super().save(inviting_user, invite_code)