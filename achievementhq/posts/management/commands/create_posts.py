from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from django.contrib.auth.models import User
from posts.models import Post

class Command(BaseCommand):
    help = 'Generate fake posts for users'

    def handle(self, *args, **kwargs):
        fake = Faker()
        users = User.objects.exclude(is_superuser=True)  # Exclude superusers if needed

        for user in users:
            # Random number of posts (0 to 20)
            num_posts = fake.random_int(min=0, max=20)
            for _ in range(num_posts):
                pub_date = fake.date_time_between(start_date=user.date_joined, end_date='now')
                # Ensure pub_date is timezone-aware
                pub_date = timezone.make_aware(pub_date)
                
                # Ensure heading_text does not exceed the maximum length of 60 characters
                heading_text = fake.sentence(nb_words=6)[:60]
                
                Post.objects.create(
                    user=user,
                    heading_text=heading_text,
                    message_text=fake.text(max_nb_chars=280),
                    pub_date=pub_date
                )
        
        self.stdout.write(self.style.SUCCESS('Successfully created fake posts for users'))
