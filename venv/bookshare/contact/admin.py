from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserProfileInfo
# Register your models here.
admin.site.register(UserProfileInfo)