from django.shortcuts import render, redirect
from .models import Personal_Feed_Post
from .forms import Create_Personal_Feed_Post_Form
from django.contrib import messages
# Straying from class based views, creating my own functions


def personal_feed_view(request):
    return render(request, "personal_feed.html")


def create_blog_view(request):

    context = {}
    user = request.user

    form = Create_Personal_Feed_Post_Form(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.author = user
        obj.save()
        form = Create_Personal_Feed_Post_Form()

        #adding a server response to assure the user the post has been sent and redirecting to feed
        messages.success(request, 'Innlegget er blitt lagt ut')
        response = redirect('personal_feed:personal_feed')
        return response

    context['form'] = form

    return render(request, "create_blog.html", context)