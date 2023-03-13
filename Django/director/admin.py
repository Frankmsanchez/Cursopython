from django.contrib import admin
from .models import Director, Pelicula

class DirectorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_nacimiento', 'nacionalidad')
    list_filter = ('nacionalidad',)
    search_fields = ('nombre', 'nacionalidad')

class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'director', 'año')
    list_filter = ('año', 'director__nacionalidad')
    search_fields = ('titulo', 'director__nombre')

admin.site.register(Director, DirectorAdmin)
admin.site.register(Pelicula, PeliculaAdmin)

