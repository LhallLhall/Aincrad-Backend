from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# from .models import User
class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Game)
admin.site.register(GameUser)
