# Generated by Django 3.2.25 on 2024-05-28 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("temas", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tema",
            name="id",
            field=models.AutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
