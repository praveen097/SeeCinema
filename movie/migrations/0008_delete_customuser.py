# Generated by Django 5.0 on 2023-12-26 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
