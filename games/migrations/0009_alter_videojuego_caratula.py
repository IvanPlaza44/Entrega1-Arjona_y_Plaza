# Generated by Django 4.1.3 on 2022-11-12 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0008_merge_20221112_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videojuego',
            name='caratula',
            field=models.ImageField(blank=True, null=True, upload_to='avatares'),
        ),
    ]
