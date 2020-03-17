from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from .models import Challenge, KnitNight
from django.contrib import messages
from .forms import CreateChallenge, CreateKnit
from accounts.models import CustomUser
from django.db.models import F


# Show a table of challenges
def challengeView(request):
    challenges = Challenge.objects.all()  # Get all the challenges in the database

    context = {
        'challenges': challenges,
    }
    return render(request, 'challenge.html', context)


# Shows a detailed view of the challenge
def challenge_detail(request, pk):
    challenges = Challenge.objects.get(pk=pk)  # Using the primary key/ID to get the requested challenge
    count = Challenge.objects.values('participants').filter(pk=pk).exclude(
        participants__isnull=True).count()  # Counts the participants for a challenge
    current_user = request.user

    if request.method == "POST":
        challenges.save()
        challenges.participants.add(current_user)  # Add the current logged in user to participants
        messages.success(request, 'Du er påmeldt!')

    context = {
        'challenges': challenges,
        'count': count
    }
    return render(request, 'challenge_detail.html', context)


# Create challenge
def create_challenge(request):
    current_user = request.user  # Get the currently logged in user
    if request.method == "POST":
        form = CreateChallenge(request.POST)
        if form.is_valid():
            b = current_user
            a = form.cleaned_data["challenge_name"]
            t = form.cleaned_data["description"]
            d = form.cleaned_data["rec_user_level"]
            f = Challenge(created_by=b, challenge_name=a, description=t, rec_user_level=d)
            f.save()

            return redirect('arr')
        else:
            messages.error(request, 'Fyll ut alle feltene!!')

    else:
        form = CreateChallenge()

    return render(request, "create_challenge.html", {"form": form})


def deregister_challenge(request, pk):
    # Deregister from a challenge
    challenges = Challenge.objects.get(pk=pk)
    challenges.save()
    challenges.participants.remove(request.user)  # Add the current logged in user to participants

    return redirect("my_page")


def my_page(request):
    mychallenges = Challenge.objects.filter(
        participants=request.user)  # Get all the challenges which have the logged in user as a participant
    myknit = KnitNight.objects.filter(
        participants=request.user)  # Get all the challenges which have the logged in user as a participant

    context = {
        'mychallenges': mychallenges,
        'myknit': myknit,
    }
    return render(request, "my_page.html", context)


# When user click on complete challenge
def complete_challenge(request):
    us = request.user
    challenges = CustomUser.objects.values('completed_challenges').filter(
        username=us)  # Get the value of completed challenges based on username
    challenges.update(completed_challenges=F('completed_challenges') + 1)  # Increment the completed challenges by 1

    # for challenge in challenges:
    #     val = challenge['completed_challenges']
    #     chall = CustomUser.objects.values('completed_challenges').filter(username=us)

    messages.success(request, 'Du har fullført utfordringen!')
    return redirect("my_page")


def knitView(request):
    knit = KnitNight.objects.all()  # Get all the challenges in the database

    context = {
        'knit': knit,
    }
    return render(request, 'knit/knit.html', context)


# Shows a detailed view of the challenge
def knit_detail(request, pk):
    challenges = KnitNight.objects.get(pk=pk)  # Using the primary key/ID to get the requested challenge
    count = KnitNight.objects.values('participants').filter(pk=pk).exclude(
        participants__isnull=True).count()  # Counts the participants for a challenge
    current_user = request.user

    if request.method == "POST":
        challenges.save()
        challenges.participants.add(current_user)  # Add the current logged in user to participants
        messages.success(request, 'Du er påmeldt!')

    context = {
        'challenges': challenges,
        'count': count
    }
    return render(request, 'knit/knit_detail.html', context)


# Create challenge
def create_knit(request):
    current_user = request.user  # Get the currently logged in user
    if request.method == "POST":
        form = CreateKnit(request.POST)
        if form.is_valid():
            b = current_user
            a = form.cleaned_data["knit_name"]
            t = form.cleaned_data["description"]
            d = form.cleaned_data["time"]
            f = KnitNight(created_by=b, knit_name=a, description=t, time=d)
            f.save()

            return redirect('knit')
        else:
            messages.error(request, 'Fyll ut alle feltene!!')

    else:
        form = CreateKnit()

    return render(request, "knit/create_knit.html", {"form": form})

# def join_challenge(request):
#     current_user = request.user  # Get the currently logged in user
#     challengeid = Challenge.objects.get(pk=pk)
#
#     context = {}
#
#     # fetch the object related to passed id
#     obj = get_object_or_404(Challenge, challengeid)
#
#     # pass the object as instance in form
#     form = CreateChallenge(request.POST or None, instance=obj)
#
#     # save the data from the form and
#     # redirect to detail_view
#     if form.is_valid():
#         b = current_user
#         form = Challenge(participants=b)
#         form.save()
#         messages.success(request, 'Melding sendt!')
#         return redirect('arr')
#
#     else:
#         messages.error(request, 'Fyll ut alle feltene!!')
#
#         # add form dictionary to context
#     context["form"] = form
#
#     return render(request, "challenge_detail.html", context)


# challenges_names = list()
#
# for challenge in challenges:
#     challenges_names.append(challenge.challenge_name)
#
# response_html = '<br>'.join(challenges_names)
#
# return HttpResponse(response_html)
