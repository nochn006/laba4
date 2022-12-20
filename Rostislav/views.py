from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from django.views.generic import CreateView
from .models import Films, Category
from .forms import FilmForm


# Create your views here.
def index(request):
    films = Film.objects.all()
    return render(request, 'film/index.html', {'films': films})


def add(request):
    if Category.objects.all().count() == 0:
        Category.objects.create(genre='комедия')
    if request.method == 'POST':
        film = Film()
        film.name = request.POST.get('name')
        film.genre = request.POST.get('genre')
        film.issue_date = request.POST.get('issue_date')
        film.actors = request.POST.get('actors')
        film.show_date = request.POST.get('show_date')
        return redirect('home')
    else:
        categories = Category.objects.all()
        film = FilmForm()
        return render(request, 'film/add.html', {'form': film, 'category': category})


def edit(request, id):
    try:
        film = Film.objects.get(id=id)
        if request.method == 'POST':
            film.name = request.POST.get('name')
            film.genre = request.POST.get('genre')
            film.issue_date = request.POST.get('issue_date')
            film.actors = request.POST.get('actors')
            film.show_date = request.POST.get('show_date')
            return redirect('home')
        else:
            categories = Category.objects.all()
            return render(request, 'edit.html', {'film': film, 'categories': categories})
    except film.DoesNotExist:
        return HttpResponseNotFound('Film not found')


def delete(request):
    return redirect('home')

