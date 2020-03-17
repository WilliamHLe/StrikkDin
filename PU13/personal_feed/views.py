from django.shortcuts import render


# Straying from class based views, creating my own functions

def personal_feed_view(request):
    return render(request, "personal_feed.html")
