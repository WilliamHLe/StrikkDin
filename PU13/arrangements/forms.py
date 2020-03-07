from django import forms


# Form for creating a challenge
class CreateChallenge(forms.Form):
    challenge_name = forms.CharField(label="Utfordring", max_length="200")
    description = forms.CharField(widget=forms.Textarea, label="Beskrivelse", max_length="500")
    rec_user_level = forms.CharField(label="Anbefalt brukernivå", max_length="200")
