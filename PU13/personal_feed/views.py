from operator import attrgetter

import get as get
from django.shortcuts import render, redirect, get_object_or_404
from .models import Personal_Feed_Post
from .forms import Create_Personal_Feed_Post_Form
from django.http import HttpResponseRedirect


# Straying from class based views, creating my own functions


def personal_feed_view(request):
    context = {}
    feed_posts = sorted(Personal_Feed_Post.objects.filter(author=request.user),key=attrgetter('date_published'), reverse=True)
    context['posts'] = feed_posts
    return render(request, "personal_feed.html", context)


def create_blog_view(request):
    context = {}
    user = request.user

    form = Create_Personal_Feed_Post_Form(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.author = user
        obj.save()
        return HttpResponseRedirect("/personal_feed/personal_feed")

    context['form'] = form

    return render(request, "create_blog.html", context)


def detail_blog_view(request, slug):
    context = {}
    feed_post = get_object_or_404(Personal_Feed_Post, slug=slug)
    context['feed_post'] = feed_post

    return render(request, 'detail_feed.html', context)
