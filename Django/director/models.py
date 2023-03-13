from django.db import models

class Director(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='directores')

    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    sinopsis = models.TextField()
    año = models.IntegerField()
    duracion = models.IntegerField()
    foto = models.ImageField(upload_to='peliculas')

    def __str__(self):
        return self.titulo

