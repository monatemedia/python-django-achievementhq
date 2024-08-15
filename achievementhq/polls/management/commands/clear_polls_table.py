from django.core.management.base import BaseCommand
from polls.models import Question, Choice

class Command(BaseCommand):
    help = 'Clear all data from the polls app.'

    def handle(self, *args, **kwargs):
        # Clear all data
        Choice.objects.all().delete()
        Question.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Successfully cleared all data from the polls app.'))
