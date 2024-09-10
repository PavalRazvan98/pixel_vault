from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from apps.games.models import Game
from apps.feedback.models import Rating
from faker import Faker


User = get_user_model()
f = Faker()

class Command(BaseCommand):
    help = "Populate the \"feedback\" database with sample ratings."

    def handle(self, *args, **kwargs):
        if Rating.objects.count() >= 5 or User.objects.count() >= 20:
            self.stdout.write(
                "There are enough `Ratings in the database, going to use them. "
            )
        else:

            ratings = []
            for g in Game.objects.all():
                for u in User.objects.all():
                    if f.pybool(25):
                        continue
                    rating = Rating(
                        game=g,
                        user=u,
                        content=f.text(max_nb_chars=120),
                        score=f.pyint(min_value=0, max_value=5),
                        submitted_review=f.date()
                    )
                    ratings.append(rating)
            try:
                Rating.objects.bulk_create(ratings)
                self.stdout.write(self.style.SUCCESS('Successfully created sample feedback.'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error creating feedback: {str(e)}'))
