from django.db import models

class Genero(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Musica(models.Model):
    titulo = models.CharField(max_length=200)
    artista = models.CharField(max_length=200)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    letra = models.TextField()
    arquivo_audio = models.FileField(upload_to='musicas/')

    def __str__(self):
        return self.titulo

class PastaMusica(models.Model):
    nome = models.CharField(max_length=200)
    musicas = models.ManyToManyField(Musica, related_name='pastas')

    def __str__(self):
        return self.nome
