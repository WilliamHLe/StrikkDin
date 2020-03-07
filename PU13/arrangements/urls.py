from django.urls import path
from . import views

urlpatterns = [
    path("arr/", views.challengeView, name="arr"),
    path("arr/<int:pk>/", views.challenge_detail, name="challenge_detail"),
    # Link to detailed challenge view based on challenge ID
    path("arr/create/", views.create_challenge, name="create_challenge")

]
