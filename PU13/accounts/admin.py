from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import MyUserCreationForm, MyUserChangeForm
from .models import CustomUser

# Viser hvilke felter av modellen som skal vises i admin-siden
class MyUserAdmin(UserAdmin):
    """
    UserAdmin er en Django-klasse som inneholder ferdig-implementerte attributter og funksjoner.
    Det gir allerede generiske funksjonaliteter knyttet til hva en Admin kan gjøre.
    Ctrl + left-click på UserAdmin for å se hvordan klassen UserAdmin ser ut.

    Attributtene 'add_form' og 'form' referer til vår egendefinerte forms (accounts/forms.py).
    Det samme gjør 'model' som knyttes til CustomUser (accounts/models.py).
    List_display viser hvilket felter som synliggjøres på Admin-apnelet.
    Fieldsets legger til ekstra felter for Admin-kontoen som ikke eksisterer i en generisk Admin-konto.
    """

    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = CustomUser
    list_display = ['username', 'name', 'user_level', 'is_Company', 'completed_challenges']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('name', 'user_level', 'is_Company', 'completed_challenges')}),
    )  # this will allow to change these fields in admin module
#Fjernet is_User fra fieldsets og list_display

"""Kobler vår modell av brukeren (CustomUser) og Admin-klassen (MyUserAdmin) som utgjør Admin-panelet"""
admin.site.register(CustomUser, MyUserAdmin)
