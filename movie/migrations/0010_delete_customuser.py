# Generated by Django 5.0 on 2023-12-26 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0009_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
