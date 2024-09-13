from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from faker import Faker

User = get_user_model()

f = Faker()


class Command(BaseCommand):
    help = "Populate the database with 15 fake users"

    def handle(self, *args, **options):
        if User.objects.filter(is_superuser=False, is_staff=False).count() != 0:
            self.stdout.write(
                "There are enough Users in the database, going to use them. ",
            )
        else:
            users = [
                User(
                    username=f.user_name(),
                    first_name=f.first_name(),
                    last_name=f.last_name(),
                    email=f.email(),
                )
                for _ in range(15)
            ]
            User.objects.bulk_create(users)
            self.stdout.write(self.style.SUCCESS("Successfully created 15 users"))
