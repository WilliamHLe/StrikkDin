from django.urls import path
from .views import SignUpView

urlpatterns = [
    path('registrer/', SignUpView.as_view(), name='signup'),
]