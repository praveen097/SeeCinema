from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView
from .models import Movie
from .forms import MovieForm

@login_required
def home_page(request):
    return render(request, 'index.html')

@login_required
def movie_list(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'movie/movie_list.html', context)

@login_required
def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    context = {'movie': movie}
    return render(request, 'movie/movie_detail.html', context)

@login_required
def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the movie list after successful creation
            return redirect('movie_list')
    else:
        form = MovieForm()

    context = {'form': form}
    return render(request, 'movie/movie_create.html', context)

def movie_edit(request, pk):
    movie = get_object_or_404(Movie, pk=pk)

    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            # Redirect to the movie detail page after successful edit
            return redirect('movie_detail', pk=pk)
    else:
        form = MovieForm(instance=movie)

    context = {'form': form, 'movie': movie}
    return render(request, 'movie/movie_edit.html', context)

@login_required
def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)

    if request.method == 'POST':
        movie.delete()
        # Redirect to the movie list after successful deletion
        return redirect('movie_list')

    context = {'movie': movie}
    return render(request, 'movie/movie_delete.html', context)