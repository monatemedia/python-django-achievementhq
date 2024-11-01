from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from decouple import config

class Command(BaseCommand):
    help = 'Create superuser if it does not exist'

    def handle(self, *args, **kwargs):
        username = config('ADMIN_USER')
        email = config('ADMIN_EMAIL')
        password = config('ADMIN_PASSWORD')

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f'Superuser {username} created successfully.'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Superuser {username} already exists.'))
