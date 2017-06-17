# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponse, Http404
from app.models import Movie, Review

# Create your views here.
def home(request):
    movie_list = Movie.objects.all()
    paginator = Paginator(movie_list, 2) # Show 2 movies per page

    page = request.GET.get('page')
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        movies = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        movies = paginator.page(paginator.num_pages)
    return render(request, 'home.html', {'movies': movies})

def movie(request, pk):
    if request.method == 'POST':
        if request.user.is_authenticated():
            pass
    elif request.method == 'GET':
        movie = Movie.objects.get(pk=pk)
        return render(request, 'movie.html', {'movie': movie})
    else:
        raise Http404("Poll does not exist")