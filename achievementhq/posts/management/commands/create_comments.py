from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from django.contrib.auth.models import User
from posts.models import Post, Comment

class Command(BaseCommand):
    help = 'Generate fake comments for posts'

    def handle(self, *args, **kwargs):
        fake = Faker()
        posts = Post.objects.all()

        if not posts.exists():
            self.stdout.write(self.style.WARNING('No posts found. Please create posts before running this script.'))
            return

        users = User.objects.exclude(is_superuser=True)
        if not users.exists():
            self.stdout.write(self.style.WARNING('No non-superuser users found. Please create users before running this script.'))
            return

        for post in posts:
            # Random number of comments (0 to 20)
            num_comments = fake.random_int(min=0, max=20)
            for _ in range(num_comments):
                pub_date = fake.date_time_between(start_date=post.pub_date, end_date='now')
                # Ensure pub_date is timezone-aware
                pub_date = timezone.make_aware(pub_date, timezone.get_current_timezone())
                Comment.objects.create(
                    user=fake.random_element(elements=users),  # Random user
                    post=post,
                    comments_text=fake.text(max_nb_chars=280),
                    pub_date=pub_date
                )
        
        self.stdout.write(self.style.SUCCESS('Successfully created fake comments for posts'))
