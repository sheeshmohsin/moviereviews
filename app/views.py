# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import NoReverseMatch, reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from app.models import Movie, Review
from app.forms import MovieForm, ReviewForm

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
        movie = Movie.objects.get(pk=pk)
        form_obj = ReviewForm(request.POST)
        if form_obj.is_valid():
            db_obj = form_obj.save(commit=False)
            db_obj.movie = movie
            if request.user.is_authenticated():
                db_obj.added_by = request.user
            db_obj.save()
            pk_value = db_obj.pk
            return HttpResponseRedirect(reverse('movie_detail', args=(pk,)))
        else:
            reviews = paginate_reviews(request, movie)
            return render(
                            request, 'movie.html', 
                            {'movie': movie, 'form': form, 'reviews': reviews}
                        )
    elif request.method == 'GET':
        movie = Movie.objects.get(pk=pk)
        form = ReviewForm()
        reviews = paginate_reviews(request, movie)
        return render(request, 'movie.html', {'movie': movie, 'form': form, 'reviews': reviews})
    else:
        raise Http404("Request method type not defined")

@login_required
def add_movie(request):
    if request.method == 'POST':
        form_obj = MovieForm(request.POST, request.FILES)
        if form_obj.is_valid():
            db_obj = form_obj.save(commit=False)
            db_obj.added_by = request.user
            db_obj.save()
            pk_value = db_obj.pk
            return HttpResponseRedirect(reverse('movie_detail', args=(pk_value,)))
        else:
            return render(request, 'add_movie.html', {'form': form_obj})
    form = MovieForm()
    return render(request, 'add_movie.html', {'form': form})


def paginate_reviews(request, movie):
    review_list = Review.objects.filter(movie=movie)
    paginator = Paginator(review_list, 2) # Show 2 movies per page

    page = request.GET.get('page')
    try:
        reviews = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        reviews = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        reviews = paginator.page(paginator.num_pages)
    return reviews

