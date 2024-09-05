from rest_framework import viewsets
from .models import Genero, Musica, PastaMusica
from .serializers import GeneroSerializer, MusicaSerializer, PastaMusicaSerializer

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

class MusicaViewSet(viewsets.ModelViewSet):
    queryset = Musica.objects.all()
    serializer_class = MusicaSerializer

class PastaMusicaViewSet(viewsets.ModelViewSet):
    queryset = PastaMusica.objects.all()
    serializer_class = PastaMusicaSerializer
