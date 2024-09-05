from rest_framework import serializers
from .models import Genero, Musica, PastaMusica

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'

class MusicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musica
        fields = '__all__'

class PastaMusicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PastaMusica
        fields = '__all__'
