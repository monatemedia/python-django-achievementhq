from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create superuser if it does not exist'

    def handle(self, *args, **kwargs):
        username = 'admin'
        email = 'admin@gmail.com'
        password = 'PennantFernlikeAnnouncerSubsidy'

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f'Superuser {username} created successfully.'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Superuser {username} already exists.'))
