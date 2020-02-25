from django.shortcuts import render

# Create your views here.
from .forms import SendMessageToAdmin
from .models import Messages1

def home(response):
    if response.method == "POST":
        form = SendMessageToAdmin(response.POST)
        if form.is_valid():
            t = form.cleaned_data["subject"]
            d = form.cleaned_data["description"]
            f = Messages1(subject=t, description=d)
            f.save()
    else:
        form = SendMessageToAdmin()

    return render(response, "contactAdmin.html", {"form":form})

