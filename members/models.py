from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime

# Create your models here.

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True)
    school = models.CharField(max_length=200, blank=True)
    department = models.CharField(max_length=200, blank=True)
    level = models.CharField(max_length=50, blank=True)
    chapter = models.CharField(max_length=100, blank=True)
    passport_photo = models.ImageField(upload_to='members/passport/', blank=True)
    membership_id = models.CharField(max_length=20, unique=True, blank=True, null=True)
    qr_code_image = models.ImageField(upload_to='members/qrcodes/', blank=True)
    id_card_generated_at = models.DateTimeField(null=True, blank=True)
    emergency_contact = models.CharField(max_length=100, blank=True)
    emergency_phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username

@receiver(post_save, sender=Member)
def generate_membership_id(sender, instance, created, **kwargs):
    if created and not instance.membership_id:
        year = datetime.now().year
        count = Member.objects.filter(membership_id__isnull=False).count() + 1
        instance.membership_id = f'NAAS-ANKPA-{year}-{count:04d}'
        instance.save()
