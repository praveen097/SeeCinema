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
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE, verbose_name = u"Name of the Theatre")
    name = models.CharField(max_length=512, verbose_name = u"Name of the Screen")
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

class Block(models.Model):
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE, related_name='blocks', verbose_name='Screen')
    name = models.CharField(max_length=512, verbose_name="Name of the block")
    seating_type = models.CharField(max_length=20, choices=SEAT_TYPE, verbose_name="Seating Type")
    price = models.PositiveIntegerField(default=0, verbose_name="Price of seats in the Block")
    no_of_rows = models.PositiveIntegerField(default=0, verbose_name="Number of rows in the Block")
    no_of_columns = models.PositiveIntegerField(default=0, verbose_name="Number of columns in the Block")

    class Meta:
        verbose_name_plural = 'Screens | Blocks'

    def __str__(self):
        return '%s' % self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Delete existing seats
        self.seats.all().delete()

        # Create seats based on the updated number of rows and columns
        for row in range(1, self.no_of_rows + 1):
            row_label = chr(65 + row - 1)
            for col in range(1, self.no_of_columns + 1):
                seat_number = f'{row_label}-{col}'
                Seat.objects.create(block=self, seat_number=seat_number, price=self.price)

class Seat(models.Model):
    block = models.ForeignKey(Block, on_delete=models.CASCADE, related_name='seats', verbose_name='Block')
    seat_number = models.CharField(max_length=10, verbose_name='Seat Number')
    price = models.PositiveIntegerField(default=0, verbose_name="Price of the Seat")

    class Meta:
        verbose_name_plural = 'Screens | Seats'
        unique_together = ('block', 'seat_number')  # Ensure uniqueness within each block

    def __str__(self):
        return '%s' % self.seat_number