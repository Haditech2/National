from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Create a superuser if one does not exist'

    def handle(self, *args, **options):
        username = 'admin'
        email = 'admin@naas.org'
        password = 'NaasAdmin2025!'
        
        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING(f'Superuser "{username}" already exists'))
            # Update password if user exists
            user = User.objects.get(username=username)
            user.set_password(password)
            user.is_staff = True
            user.is_superuser = True
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Password updated for "{username}"'))
        else:
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" created successfully'))
        
        self.stdout.write(self.style.SUCCESS(f'\nAdmin Login Details:'))
        self.stdout.write(f'URL: /admin/')
        self.stdout.write(f'Username: {username}')
        self.stdout.write(f'Password: {password}')
