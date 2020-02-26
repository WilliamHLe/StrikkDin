from django.shortcuts import render

# Create your views here.
from .forms import SendMessageToAdmin
from .models import Messages1

def home(response):
    if response.method == "POST":
        form = SendMessageToAdmin(response.POST)
        if form.is_valid():
            a = form.cleaned_data["text_from"]
            t = form.cleaned_data["subject"]
            d = form.cleaned_data["description"]
            f = Messages1(text_from=a, subject=t, description=d)
            f.save()
    else:
        form = SendMessageToAdmin()

    return render(response, "contactAdmin.html", {"form":form})

