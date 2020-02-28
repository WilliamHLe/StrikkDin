from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import MyUserCreationForm, MyUserChangeForm
from .models import CustomUser


class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = CustomUser
    list_display = ['username', 'name', 'user_level', 'is_Company']
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('name', 'user_level', 'is_Company')}),
    )  # this will allow to change these fields in admin module
#Fjernet is_User fra fieldsets og list_display

admin.site.register(CustomUser, MyUserAdmin)
