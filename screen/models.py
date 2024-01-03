from django.db import models
from theatre.models import Theatre

# Create your models here.
STATUS = (
    ('active', 'Active'),
    ('inactive', 'Inactive'),
    ('maintenance', 'Under Maintenance')
)
SCREEN_TYPE = (
    ('small', 'Small'),
    ('medium', 'Medium')
)

class Screen(models.Model):
    name = models.CharField(max_length=512, verbose_name = u"Name of the Screen")
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE, verbose_name = u"Name of the Theatre")
    satus = models.CharField(max_length=512, choices=STATUS, default= 'active', verbose_name = u"Status of the Screen")
