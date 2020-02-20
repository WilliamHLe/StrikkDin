
from django import forms


class SendMessageToAdmin(forms.Form):
    subject = forms.CharField(label="Emne", max_length="200")
    description = forms.CharField(widget=forms.Textarea, label="Beskrivelse", max_length="500")
