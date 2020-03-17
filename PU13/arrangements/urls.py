from django.urls import path
from . import views

urlpatterns = [
    path("utfordring/", views.challengeView, name="arr"),
    path("utfordring/<int:pk>/", views.challenge_detail, name="challenge_detail"),

    # Link to detailed challenge view based on challenge ID
    path("utfordring/opprett/", views.create_challenge, name="create_challenge"),

    path("strikkekveld/", views.knitView, name="knit"),
    path("strikkekveld/opprett/", views.create_knit, name="create_knit"),
    path("strikkekveld/<int:pk>/", views.knit_detail, name="knit_detail"),

    path("minside/", views.my_page, name="my_page"),
    path("minside/<int:pk>/", views.deregister_challenge, name="delete"),
    path("minside/d", views.complete_challenge, name="complete"),
]
