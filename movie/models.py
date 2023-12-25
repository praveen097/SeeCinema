from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta

# Create your models here.
def validate_future_date(value):
    if value < timezone.now().date():
        raise ValidationError('Release date must be in the future.')
    
class Movie(models.Model):
    name = models.CharField(max_length=512, verbose_name=u'Name of the Movie')
    director = models.CharField(max_length=512, verbose_name=u'Name of the Director')
    is_published = models.BooleanField(default=False, verbose_name='Publish the Movie')
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    release_date = models.DateField(validators=[validate_future_date])
    total_time_minutes = models.IntegerField(null=True, verbose_name='Total Time (in minutes)')
    poster = models.ImageField(upload_to='movie_posters/', null=True, blank=True)



    class Meta:
        verbose_name_plural = 'Movies'
        ordering = ['-created_on']

    def __str__(self):
        return '%s' % self.name
    @property
    def total_time(self):
        # Convert total_time_minutes to a timedelta object representing minutes
        return timedelta(minutes=self.total_time_minutes)
