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
    ('medium', 'Medium'),
    ('large', 'Large')
)
SEAT_TYPE = (
    ('normal', 'Normal'),
    ('recliner', 'Recliner')
)
PRICE_CATEGORIES = (
    ('standard','Standard'),
    ('premium', 'Premium'),
)

class Screen(models.Model):
    name = models.CharField(max_length=512, verbose_name = u"Name of the Screen")
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE, verbose_name = u"Name of the Theatre")
    status = models.CharField(max_length=512, choices=STATUS, default= 'active', verbose_name = u"Status of the Screen")
    screen_type = models.CharField(max_length=512, choices=SCREEN_TYPE, default='small', verbose_name = u"Type of the Screen")
    capacity = models.PositiveIntegerField(verbose_name=u"Capacity")
    description = models.TextField(blank=True, null=True, verbose_name=u"Description")
    is_3d_capable = models.BooleanField(default=False, verbose_name=u"3D Capability")
    is_wheelchair_accessible = models.BooleanField(default=False, verbose_name=u"Wheelchair Accessibility")
    audio_type = models.CharField(max_length=512, verbose_name="Audio type")
    last_maintenance_date = models.DateField(null=True, blank=True, verbose_name=u"Last Maintenance Date")
    price_category = models.CharField(max_length=20, choices=PRICE_CATEGORIES, default='standard', verbose_name=u"Price Category")

    class Meta:
        verbose_name_plural = 'Screens'

    def __str__(self):
        return '%s' % self.name




class Seat(models.Model):
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE, related_name='seats', verbose_name='Screen')
    seat_number = models.CharField(max_length=10, verbose_name='Seat Number')
    seat_type = models.CharField(max_length = 20, verbose_name="Type of Seat")

    class Meta:
        verbose_name_plural = 'Seats'

    def __str__(self):
        return '%s' % self.name

