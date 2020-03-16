from django.urls import path
from . import views

urlpatterns = [
    path("utfordring/", views.challengeView, name="arr"),
    path("utfordring/<int:pk>/", views.challenge_detail, name="challenge_detail"),

    # Link to detailed challenge view based on challenge ID
    path("utfordring/opprett/", views.create_challenge, name="create_challenge"),

    path("minside/", views.my_page, name="my_page"),
    path("minside/<int:pk>/", views.deregister_challenge, name="delete"),
    path("minside/d", views.complete_challenge, name="complete"),
]
