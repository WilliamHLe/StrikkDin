from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from .models import Challenge
from django.contrib import messages
from .forms import CreateChallenge


# Show a table of challenges
def challengeView(request):
    challenges = Challenge.objects.all()  # Get all the challenges in the database
    return render(request, 'challenge.html', {'challenges': challenges})


# Shows a detailed view of the challenge
def challenge_detail(request, pk):
    challenges = Challenge.objects.get(pk=pk)  # Using the primary key/ID to get the requested challenge
    context = {
        'challenges': challenges
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
            messages.success(request, 'Melding sendt!')

            response = redirect('arr')
            return response
        else:
            messages.error(request, 'Fyll ut alle feltene!!')

    else:
        form = CreateChallenge()

    return render(request, "create_challenge.html", {"form": form})


# Funker ikke enda
def join_challenge(request):
    current_user = request.user  # Get the currently logged in user
    challengeid = Challenge.objects.get(pk=pk)

    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Challenge, challengeid)

    # pass the object as instance in form
    form = CreateChallenge(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect('arr')

        # add form dictionary to context
    context["form"] = form

    return render(request, "challenge_detail.html", context)

def home(request):
  return render(request, "my_page.html")

# def create_challenge(request):
#
#     if request.method == 'POST':
#         challenge_name = request.POST['challenge_name']
#         description = request.POST['description']
#         rec_user_level = request.POST['rec_user_level']
#
#         #user = settings.AUTH_USER_MODEL.objects.first()  # TODO: get the currently logged in user
#
#         chal = Challenge.objects.create(
#             challenge_name=challenge_name,
#             description=description,
#             rec_user_level=rec_user_level
#         )
#         context = {
#             'challenge_name': challenge_name,
#             'description': description,
#             'rec_user_level': rec_user_level
#         }
#         return redirect('arr')  # TODO: redirect to the created topic page
#
#     return render(request, 'create_challenge.html', context)

# challenges_names = list()
#
# for challenge in challenges:
#     challenges_names.append(challenge.challenge_name)
#
# response_html = '<br>'.join(challenges_names)
#
# return HttpResponse(response_html)
