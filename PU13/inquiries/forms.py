
from django import forms


class SendMessageToAdmin(forms.Form):
    """
    En generell form (forms.Form) som håndterer brukerinput representert av de ulike feltene nedenfor.
    """
    text_from = forms.CharField(label="Navn", max_length="200")
    subject = forms.CharField(label="Emne", max_length="200")
    description = forms.CharField(widget=forms.Textarea, label="Beskrivelse", max_length="500")
