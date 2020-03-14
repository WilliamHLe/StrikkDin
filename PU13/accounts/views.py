from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import MyUserCreationForm


from django.contrib.messages.views import SuccessMessageMixin

class SignUpView(SuccessMessageMixin, CreateView):
    form_class = MyUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    success_message = "%(username)s er registrert!"
