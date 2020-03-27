from urllib import request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import MyUserCreationForm
from django.contrib.messages.views import SuccessMessageMixin

"""
    CreateView håndterer en form (MyUserCreationForm) i ved å lage et objekt.
    I MyUserCreationForm representerer den ulike felter som CreateView vil håndtere datalagringen på disse feltene.
    template_name kobles opp mot grensesnittet ved å rendre html-filen og synliggjøres for brukeren.
    """
# Logikken bak registreringsskjemaet, bruker innebygd Django generic createview
class SignUpView(SuccessMessageMixin, CreateView):
    """SuccessMessageMixin støtter class-based-views til å håndtere suksessmeldinger på vellykde forms.
       Bruker variabelen 'sucess_message' til å skrive ut meldingen. """

    form_class = MyUserCreationForm
    success_url = reverse_lazy('login')
    success_message = "%(username)s er registrert!"
    template_name = 'registration/signup.html'
