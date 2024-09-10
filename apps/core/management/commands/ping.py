from django.core.management import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = 'Write "pong" as a response to ping'

    def handle(self, *args, **options):
        self.stdout.write("pong")
        #
        # # Citirea variabilelor de mediu
        # username = os.environ.get("PIXEL_VAULT_USERNAME")
        # password = os.environ.get("PIXEL_VAULT_PASSWORD")
        # email = os.environ.get("PIXEL_VAULT_EMAIL")
        #
        # # Afișarea valorilor
        # self.stdout.write(f"USERNAME: {username}")
        # self.stdout.write(f"PASSWORD: {password}")
        # self.stdout.write(f"EMAIL: {email}")
        # self.stdout.write("pong")