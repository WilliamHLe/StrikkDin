from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import MyUserCreationForm


class SignUpView(CreateView):
    """
    CreateView håndterer en form (MyUserCreationForm) i ved å lage et objekt.
    I MyUserCreationForm representerer den ulike felter som CreateView vil håndtere datalagringen på disse feltene.
    template_name kobles opp mot grensesnittet ved å rendre html-filen og synliggjøres for brukeren.
    """
    form_class = MyUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

