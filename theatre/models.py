from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import AbstractUser

class Theatre(models.Model):
    name = models.CharField(max_length=512, verbose_name=u'Name of the Theatre')
    owner = models.CharField(max_length=512, verbose_name=u'Name of the Owner')
    screens = models.IntegerField(null=True, verbose_name='Total Screens')
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    address = models.CharField(max_length=1024, verbose_name=u'Theatre Address')
    city = models.CharField(max_length=255, verbose_name=u'City')
    state = models.CharField(max_length=255, verbose_name=u'State')
    zip_code = models.CharField(max_length=20, verbose_name=u'ZIP Code')
    phone_number = models.CharField(max_length=20, verbose_name=u'Phone Number')
    email = models.EmailField(max_length=255, verbose_name=u'Email Address')
    opening_time = models.TimeField(null=True, verbose_name='Opening Time')
    closing_time = models.TimeField(null=True, verbose_name='Closing Time')
    logo = models.ImageField(upload_to='theatre_logos/', null=True, blank=True, verbose_name='Theatre Logo')
    description = models.TextField(null=True, blank=True, verbose_name='Description')
    directions_link = models.URLField(max_length=512, null=True, blank=True, verbose_name='Directions Link')



