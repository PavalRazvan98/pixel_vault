from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Populate all databases."

    def handle(self, *args, **kwargs):
        commands = [
            "populate_misc_database",
            "populate_users_database",
            "populate_games_database",
            "populate_feedback_database",
            "populate_interaction_database",
        ]

        for command in commands:
            self.stdout.write(f"Running {command}...")
            try:
                call_command(command)
                self.stdout.write(self.style.SUCCESS(f"Successfully ran {command}."))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error running {command}: {e!s}"))
