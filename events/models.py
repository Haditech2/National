from django.db import models
from django.utils import timezone

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    venue = models.CharField(max_length=200)
    image = models.ImageField(upload_to='events/', blank=True)

    def __str__(self):
        return self.title

    @property
    def is_upcoming(self):
        return self.date > timezone.now()

    class Meta:
        ordering = ['date']

class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='gallery')
    image = models.ImageField(upload_to='events/gallery/')
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.caption or f'Image {self.id}'
