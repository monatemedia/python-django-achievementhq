from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from faker import Faker
from posts.models import Post, Comment

class Command(BaseCommand):
    help = 'Generate fake comments for posts'

    def handle(self, *args, **kwargs):
        fake = Faker()
        posts = Post.objects.all()

        for post in posts:
            # Random number of comments (0 to 20)
            num_comments = fake.random_int(min=0, max=20)
            for _ in range(num_comments):
                pub_date = fake.date_time_between(start_date=post.pub_date, end_date='now')
                Comment.objects.create(
                    user=fake.random_element(elements=User.objects.exclude(is_superuser=True)),  # Random user
                    post=post,
                    comments_text=fake.text(max_nb_chars=280),
                    pub_date=pub_date
                )
        
        self.stdout.write(self.style.SUCCESS('Successfully created fake comments for posts'))
