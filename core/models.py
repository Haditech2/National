from django.db import models
import base64

# Create your models here.

class Executive(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    school = models.CharField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='executives/', blank=True)
    photo_data = models.TextField(blank=True, help_text="Base64 encoded image for database storage")
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
    
    def get_photo_url(self):
        """Return photo URL or data URI for database-stored images"""
        if self.photo_data:
            return f"data:image/jpeg;base64,{self.photo_data}"
        elif self.photo:
            return self.photo.url
        return None
    
    def save(self, *args, **kwargs):
        # If photo file is uploaded, convert to base64 and store in photo_data
        if self.photo:
            try:
                self.photo.seek(0)
                image_data = self.photo.read()
                self.photo_data = base64.b64encode(image_data).decode('utf-8')
            except:
                pass
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['order']
