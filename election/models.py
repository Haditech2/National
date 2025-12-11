from django.db import models

# Create your models here.

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    level = models.CharField(max_length=50)
    department = models.CharField(max_length=100)
    manifesto = models.FileField(upload_to='manifestos/', blank=True)
    photo = models.ImageField(upload_to='candidates/', blank=True)
    manifesto_text = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name} - {self.position}'
