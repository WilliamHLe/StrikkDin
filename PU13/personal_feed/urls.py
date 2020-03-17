from django.urls import path

from . import views

urlpatterns = [
    path("personal_feed/", views.personal_feed_view, name ="personal_feed")
]