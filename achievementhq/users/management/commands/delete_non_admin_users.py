from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Delete all users except administrators'

    def handle(self, *args, **kwargs):
        # Get all users except those with is_superuser=True
        users_to_delete = User.objects.exclude(is_superuser=True)

        # Count of users to be deleted
        count = users_to_delete.count()

        if count > 0:
            # Delete the users
            users_to_delete.delete()
            self.stdout.write(self.style.SUCCESS(f'Successfully deleted {count} non-admin users'))
        else:
            self.stdout.write(self.style.SUCCESS('No non-admin users found to delete'))
