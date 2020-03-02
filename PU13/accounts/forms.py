from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

# Lager form class som brukes for å lage html form/skjema

# Viser hva registreringsskjemaet skal inneholde
class MyUserCreationForm(UserCreationForm):
    choi = (('Nybegynner', 'Nybegynner'), ('Erfaren', 'Erfaren'), ('Proff', 'Proff'),)
    user_level = forms.ChoiceField(choices=choi)

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'name', 'user_level', 'is_User', 'is_Company')

# Aktiverer feltene som vises
class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('username', 'name', 'user_level', 'is_Company')


