from django.contrib import admin
from .models import Genero, Musica, PastaMusica

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    pass

@admin.register(Musica)
class MusicaAdmin(admin.ModelAdmin):
    pass

@admin.register(PastaMusica)
class PastaMusicaAdmin(admin.ModelAdmin):
    pass
