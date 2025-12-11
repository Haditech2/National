from django.db import models

# Create your models here.

class Executive(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    school = models.CharField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='executives/', blank=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']
