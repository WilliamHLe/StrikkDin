from django.shortcuts import render
from .models import Personal_Feed_Post
from .forms import Create_Personal_Feed_Post_Form

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

    context['form'] = form

    return render(request, "create_blog.html", context)