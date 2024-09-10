from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from apps.games.models import Game
from apps.interactions.models import Session
from faker import Faker
from datetime import timedelta

User = get_user_model()
f = Faker()


class Command(BaseCommand):
    help = "Populate the \"interactions\" database with sample sessions."

    def handle(self, *args, **kwargs):
        if Session.objects.count() >= 5 or User.objects.count() >= 20:
            self.stdout.write(
                "There are enough `Sessions` in the database, going to use them. "
            )
        else:
            sessions = []

            for g in Game.objects.all():
                for u in User.objects.all():
                    if f.pybool(25):
                        continue
                    session = Session(
                        game=g,
                        user=u,
                        last_play=f.date_time_this_year(),
                        time_play=timedelta(minutes=f.random_int(min=30, max=120)),
                        ip_address=f.ipv4()
                    )
                    sessions.append(session)
            try:
                Session.objects.bulk_create(sessions)
                self.stdout.write(self.style.SUCCESS('Successfully created sample sessions.'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error creating sessions: {str(e)}'))
