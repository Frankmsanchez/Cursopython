from django import views
from django.urls import path


urlpatterns = [
    path('', views.director_list, name='director_list'),
    path('directores/<int:pk>/', views.director_detail, name='director_detail'),
    path('peliculas/', views.pelicula_list, name='pelicula_list'),
]