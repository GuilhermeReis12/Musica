# Generated by Django 3.2.25 on 2024-05-29 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("person", "0002_remove_person_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="data_nascimento",
            field=models.DateField(blank=True, null=True),
        ),
    ]
