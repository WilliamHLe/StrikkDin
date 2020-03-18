from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class MyUserCreationForm(UserCreationForm):
    """Tar inn UserCreationForm-klassen som allerede har feltene 'Username', 'Password1' og 'Password2'
       Definerer feltet user_level til å være ChoiceField slik at man kan velge flere alternativer.
       Choi er hvilke brukernivåer brukeren kan velge mellom.
       Det er representert som en tuppel (Element1, Element2) slik at Element1 er den verdien som blir satt i modellen vår (accounts/models.py)
       Element2 er det som vises for brukeren."""

    choi = (('Nybegynner', 'Nybegynner'), ('Erfaren', 'Erfaren'), ('Proff', 'Proff'),)
    user_level = forms.ChoiceField(choices=choi)

    class Meta(UserCreationForm):
        """Meta-klassen inneholder metadata eller informasjon til formen man bruker (MyUserCreationForm).
           Den konfigurer nødvendig informasjon til modellen som skal brukes (CustomUser)."""
        model = CustomUser
        fields = ('username', 'name', 'user_level', 'is_User', 'is_Company')


class MyUserChangeForm(UserChangeForm):
    """Tar inn UserChangeForm som kan gi en superbruker (Admin) til å endre på feltene på Adminsiden. """
    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('username', 'name', 'user_level', 'is_Company')


