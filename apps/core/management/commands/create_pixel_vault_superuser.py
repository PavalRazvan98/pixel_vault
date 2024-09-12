import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    help = "Create a superuser with specific attributes."

    def add_arguments(self, parser):
        parser.add_argument("--username", type=str, help="Username for the superuser")
        parser.add_argument("--password", type=str, help="Password for the superuser")
        parser.add_argument("--email", type=str, help="Email for the superuser")

    def handle(self, *args, **options):
        existing_superuser = User.objects.filter(is_superuser=True).first()

        if existing_superuser:
            self.stdout.write(
                self.style.WARNING(
                    f'There is already a superuser in the DB, the username is "{existing_superuser.username}". '
                    f'Won\'t create another superuser.',
                ),
            )
            return
        username = options["username"] or os.environ.get("PIXEL_VAULT_USERNAME")
        password = options["password"] or os.environ.get("PIXEL_VAULT_PASSWORD")
        email = options["email"] or os.environ.get("PIXEL_VAULT_EMAIL")

        User.objects.create_superuser(
            username=username,
            password=password,
            email=email,
        )

        self.stdout.write(self.style.SUCCESS(f'Successfully created superuser "{username}".'))
