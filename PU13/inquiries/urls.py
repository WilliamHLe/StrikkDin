from django.urls import path

from .views import home

# Kobler viewet home til en URL og gir ID-en 'kontakt'.
urlpatterns = [
    path("kontakt/", home, name ="kontakt")
]