from django.shortcuts import render

# Create your views here.
from .forms import SendMessageToAdmin
from .models import Inquiries

from django.shortcuts import render, redirect
#from django.http import HttpResponse, HttpResponseRedirect
#from django.urls import reverse

from django.contrib import messages

def home(request):
    """
    Et eksempel på et ikke classed-based view som medfører mer koder for å håndtere en 'response' fra brukeren - brukerinput.

    Dersom den mottar en POST-request med data som brukeren har submitted.
    POST-requesten med dataen (kan være tom) videresendes til SendMessageToAdmin slik at brukerinputen håndteres der.

    Videre valideres dataen på feltene. Gir False dersom minst et av feltene er blanke og True hvis alle feltene er fylt ut.
    cleaned_data sørger automatisk for å konvertere brukerinputen til riktig datatype.
    For eksempel et IntegerField gjøres om til integer, BooleanField til True/False osv.
    cleaned_data returnerer en dictionary der hvert felt i formen (SendMessageToAdmin) utgjør nøklene og brukerinputen er verdiene.
    I dette tilfelle så aksesserer variabelene a, t og d verdiene i dictionary som har blitt validert og konvertet til riktig datatype.
    Videre sendes den til modellen vår (Inquiries) som legger det til og lgares i databasen.

    I tillegg er det lagt til en funksjon 'messages.success()' som tar inn HTTP-request fra brukeren og en egendefinert melding.
    Det skal returnere en tilbakemelding dersom 'formen' er validert.
    Til slutt blir man rutet til 'kontakt'-siden.
    Dersom 'formen' ikke blir validert får man opp en feilmelding om at feltene ikke er fylt ut.

    Dersom det brukeren ikke submitter data, vil den rendre siden (prosessere HTML-filen) med en tom form.

    :param request: En HTTP-request fra brukeren.
    :return: 1. HTTP-response i form av prosessert HTML-fil ved at man blir redirecta til siden. 
    """
    if request.method == "POST":
        form = SendMessageToAdmin(request.POST)
        if form.is_valid():
            a = form.cleaned_data["text_from"]
            t = form.cleaned_data["subject"]
            d = form.cleaned_data["description"]
            f = Inquiries(text_from=a, subject=t, description=d)
            f.save()
            messages.success(request, 'Melding sendt!')

            response = redirect('kontakt')
            return response
        else:
            messages.error(request, 'Fyll ut alle feltene!!')

    else:
        form = SendMessageToAdmin()

    return render(request, "contactAdmin.html", {"form":form})

