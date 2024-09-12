from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    help = 'Write "pong" as a response to ping'

    def handle(self, *args, **options):
        self.stdout.write("pong")
