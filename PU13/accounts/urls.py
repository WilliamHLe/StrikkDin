from django.urls import path
from .views import SignUpView

"""
Ruter view til en url ved hjelp av path()
Det første argumentet er en string som navnet man velger selv som viewet skal rute til.
Det andre argumentet er selve viewet. SignUpView brukes her og '.as_view' brukes fordi viewet er en class-based view.
Det siste argumentet er ID-en som har blitt gitt 'singup'. Det er for å kunne referere til denne URL-en ved behov.
F.eks. kan man refere til URL-en i templates (se templates/base.html, linje 33 for dette tilfellet).
Eller så kan man også referere i koden se ekempelvis er gjort accounts/views for 'login'.
"""
urlpatterns = [
    path('registrer/', SignUpView.as_view(), name='signup'),
]