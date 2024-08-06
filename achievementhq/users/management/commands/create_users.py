from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker
from django.utils import timezone
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Generate fake users and list them'

    def handle(self, *args, **kwargs):
        fake = Faker()
        password = 'DecreasePrototypeEasiestOxidant'
        end_date = timezone.now()
        start_date = end_date - timedelta(days=5*365)

        created_users = []

        for _ in range(20):
            random_date = fake.date_between(start_date=start_date, end_date=end_date)
            random_date = timezone.make_aware(datetime.combine(random_date, datetime.min.time()))
            
            user = User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password=password
            )
            created_users.append(user)

        # List out the created users
        self.stdout.write(self.style.SUCCESS('Successfully created fake users:'))
        for user in created_users:
            self.stdout.write(f'Username: {user.username}, Password: {password}')
