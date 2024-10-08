# Generated by Django 3.2.25 on 2024-05-21 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tema",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("ds_tema", models.CharField(max_length=250)),
                ("tema", models.TextField(null=True)),
                ("ativo", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
