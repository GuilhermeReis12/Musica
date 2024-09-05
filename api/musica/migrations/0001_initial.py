# Generated by Django 5.0.6 on 2024-09-05 17:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Musica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('artista', models.CharField(max_length=200)),
                ('letra', models.TextField()),
                ('arquivo_audio', models.FileField(upload_to='musicas/')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musica.genero')),
            ],
        ),
        migrations.CreateModel(
            name='PastaMusica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('musicas', models.ManyToManyField(related_name='pastas', to='musica.musica')),
            ],
        ),
    ]
