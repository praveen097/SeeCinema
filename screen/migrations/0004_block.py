# Generated by Django 5.0 on 2024-01-04 06:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screen', '0003_delete_seat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, verbose_name='Name of the block')),
                ('seating_type', models.CharField(choices=[('normal', 'Normal'), ('recliner', 'Recliner')], max_length=20, verbose_name='Seating Type')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Price of seats in the Block')),
                ('no_of_rows', models.PositiveIntegerField(default=0, verbose_name='Number of rows in the Block')),
                ('no_of_columns', models.PositiveIntegerField(default=0, verbose_name='Number of columns in the Block')),
                ('screen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blocks', to='screen.screen', verbose_name='Screen')),
            ],
            options={
                'verbose_name_plural': 'Screens | Blocks',
            },
        ),
    ]
