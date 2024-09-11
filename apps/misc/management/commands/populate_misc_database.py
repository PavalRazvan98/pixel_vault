from django.core.management.base import BaseCommand
from apps.misc.models import Publisher, Developer, Platform, Genre, Feature, Badge


class Command(BaseCommand):
    help = "Populate the \"misc\" database."

    def handle(self, *args, **options):

        if Publisher.objects.count():
            self.stdout.write(
                "There are `Publishers` in the database, going to use them."
            )
        else:
            publishers = [
                Publisher(name="Blizzard Entertainment", nationality="USA", still_active=True),
                Publisher(name="Bethesda Softworks", nationality="USA", still_active=True),
                Publisher(name="Electronic Arts", nationality="USA", still_active=True),
                Publisher(name="Ubisoft", nationality="France", still_active=True),
                Publisher(name="Square Enix", nationality="Japan", still_active=True),
                Publisher(name="Bandai Namco Entertainment", nationality="Japan", still_active=True),
                Publisher(name="Capcom", nationality="Japan", still_active=True),
                Publisher(name="Sega", nationality="Japan", still_active=True),
                Publisher(name="Nintendo", nationality="Japan", still_active=True),
                Publisher(name="Rockstar Games", nationality="USA", still_active=True),
                Publisher(name="Naughty Dog", nationality="USA", still_active=True),
                Publisher(name="CD Projekt Red", nationality="Poland", still_active=True)
            ]
            Publisher.objects.bulk_create(publishers)

        if Developer.objects.count():
            self.stdout.write(
                "There are `Developer` in the database, going to use them."
            )
        else:
            developers = [
                Developer(name="Naughty Dog", nationality="USA", entity="Company", still_active=True),
                Developer(name="CD Projekt Red", nationality="Poland", entity="Company", still_active=True),
                Developer(name="FromSoftware", nationality="Japan", entity="Company", still_active=True),
                Developer(name="Valve Corporation", nationality="USA", entity="Company", still_active=True),
                Developer(name="Rockstar Games", nationality="UK", entity="Company", still_active=True),
                Developer(name="Ubisoft Montreal", nationality="Canada", entity="Company", still_active=True),
                Developer(name="Santa Monica Studio", nationality="USA", entity="Company", still_active=True),
                Developer(name="Bethesda Softworks", nationality="USA", still_active=True)
            ]
            Developer.objects.bulk_create(developers)

        if Platform.objects.count():
            self.stdout.write(
                "There are `Platform` in the database, going to use them."
            )
        else:
            platforms = [
                Platform(name="PlayStation 4", logo="https://banner2.cleanpng.com/20180729/gzw/09586814236b1e5c271e599460cd515d.webp"),
                Platform(name="Xbox One", logo="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/XBOX_logo_2012.svg/2560px-XBOX_logo_2012.svg.png"),
                Platform(name="Nintendo Switch", logo="https://w7.pngwing.com/pngs/485/678/png-transparent-wii-xbox-360-nintendo-switch-logo-nintendo-text-nintendo-video-game-thumbnail.png"),
                Platform(name="PC", logo="https://i.etsystatic.com/20023820/r/il/2746d9/3407675769/il_fullxfull.3407675769_l1my.jpg"),
                Platform(name="Stadia", logo="https://ssl.gstatic.com/stadia/gamers/assets/stadia_logo_and_text_v1.jpg"),
                Platform(name="PlayStation Vita", logo="https://pbs.twimg.com/profile_images/595306625998675968/s90WosHA_400x400.jpg"),
                Platform(name="iOS", logo="https://cdn.icon-icons.com/icons2/2235/PNG/512/ios_os_logo_icon_134676.png")
            ]
            Platform.objects.bulk_create(platforms)

        if Genre.objects.count():
            self.stdout.write(
                "There are `Genre` in the database, going to use them."
            )
        else:
            genres = [
                Genre(name="Action"),
                Genre(name="Adventure"),
                Genre(name="RPG"),
                Genre(name="Simulation"),
                Genre(name="Strategy"),
                Genre(name="Sports"),
                Genre(name="Puzzle"),
                Genre(name="Open World"),
                Genre(name="Moba")
            ]
            Genre.objects.bulk_create(genres)

        if Feature.objects.count():
            self.stdout.write(
                "There are `Feature` in the database, going to use them."
            )
        else:
            features = [
                Feature(name="Multiplayer"),
                Feature(name="Single Player"),
                Feature(name="Co-op"),
                Feature(name="VR Support"),
                Feature(name="Cross-Platform"),
                Feature(name="Achievements"),
                Feature(name="Open World"),
                Feature(name="Stealth"),
                Feature(name="Survival"),

                Feature(name="Leaderboards")
            ]
            Feature.objects.bulk_create(features)

        if Badge.objects.count():
            self.stdout.write(
                "There are `Badge` in the database, going to use them."
            )
        else:
            badge = [
                Badge(name="Best Game"),
                Badge(name="Editor’s Choice"),
                Badge(name="New Release"),
                Badge(name="Top Rated"),
                Badge(name="Most Anticipated Game"),
                Badge(name="Game of the Year"),
                Badge(name="Early Access")
            ]
            Badge.objects.bulk_create(badge)
