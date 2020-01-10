from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Movie, Genre

# Create your views here.

#Creates fns that takes the request from user
#and emits a response
def index(request):
    return render(request, 'biews/index.html')
"""
    read all: Movie.objects.all()
    get by id: Movie.objects.get(id=1)
    filter: Movie.objects.filter(release_year=1979)


"""

def catalog(request):
    movies = Movie.objects.all()
    #titles = ',  '.join([m.title for m in movies])
    #return HttpResponse(titles)
    return render(request, 'views/catalogetest.html', {'title': 'FROM BACKED', 'movies': movies })



def test(request):
    return HttpResponse("This is a Test")

def developer(request):
    return HttpResponse("<h1>Kevin</h1>")