import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from polls.models import Question, Choice

class Command(BaseCommand):
    help = 'Populate the database with 10 questions, each with 3 choices and random votes.'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Choice.objects.all().delete()
        Question.objects.all().delete()

        # Create 10 questions
        for i in range(5):
            question_text = f"Achievement Question {i+1}"
            pub_date = timezone.now()
            question = Question.objects.create(question_text=question_text, pub_date=pub_date)

            # Create 3 choices for each question
            for j in range(3):
                choice_text = f"Choice {j+1} for Question {i+1}"
                votes = random.randint(0, 15)
                Choice.objects.create(question=question, choice_text=choice_text, votes=votes)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with questions and choices.'))
