# Generated by Django 5.0 on 2023-12-25 15:23

import movie.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Publish the Movie'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(validators=[movie.models.validate_future_date]),
        ),
    ]
