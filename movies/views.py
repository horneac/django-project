from django.shortcuts import render
from django.http import HttpResponse
from .models import Movies
# Create your views here.
def index(request):
    #return HttpResponse('HELlo')

    movies = Movies.objects.all()
    context = {
        'title': 'Movies',
        'movies': movies
        }

    return render(request,'movies/index.html', context)

def details(request, id):

    movie = Movies.objects.get(id=id)
    context = {
        'movie': movie
        }
    return render(request,'movies/details.html',context)
