from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone_number', 'invite_code', 'inviting_user')

admin.site.register(User)
