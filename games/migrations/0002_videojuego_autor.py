# Generated by Django 4.1.2 on 2022-11-12 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='videojuego',
            name='autor',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
