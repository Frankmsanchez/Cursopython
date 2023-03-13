from django.shortcuts import render
from .models import Director, Pelicula

def director_list(request):
    directores = Director.objects.all()
    return render(request, 'director_list.html', {'directors': directores})

def director_detail(request, pk):
    director = Director.objects.get(pk=pk)
    peliculas = Pelicula.objects.filter(director=director)
    return render(request, 'director_detail.html', {'director': director, 'peliculas': peliculas})

def pelicula_list(request):
    peliculas = Pelicula.objects.all()
    return render
