from django import forms
from . import models
from .models import Personal_Feed_Post


class Create_Personal_Feed_Post_Form(forms.ModelForm):

    class Meta:
        model = Personal_Feed_Post
        fields = ['title', 'content']