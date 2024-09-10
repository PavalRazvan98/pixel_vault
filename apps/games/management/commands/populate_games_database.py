from datetime import date

from django.core.management.base import BaseCommand

from apps.games.models import Game, SystemRequirement
from apps.misc.models import Genre, Feature, Publisher, Developer, Platform, Badge


class Command(BaseCommand):
    help = 'Populate the "games" database with sample games.'

    def handle(self, *args, **options):
        if Game.objects.count():
            self.stdout.write(
                "There are `Games` in the database, going to use them. "
            )
        else:
            action_genre = Genre.objects.get(name="Action")
            adventure_genre = Genre.objects.get(name="Adventure")
            rpg_genre = Genre.objects.get(name="RPG")

            stealth_feature = Feature.objects.get(name="Stealth")
            survival_feature = Feature.objects.get(name="Survival")
            open_world_feature = Feature.objects.get(name="Open World")

            naughty_dog_publisher = Publisher.objects.get(name="Naughty Dog")
            cd_projekt_publisher = Publisher.objects.get(name="CD Projekt Red")
            bethesda_publisher = Publisher.objects.get(name="Bethesda Softworks")
            rockstar_publisher = Publisher.objects.get(name="Rockstar Games")

            naughty_dog_developer = Developer.objects.get(name="Naughty Dog")
            bethesda_developer = Developer.objects.get(name="Bethesda Softworks")
            cd_projekt_developer = Developer.objects.get(name="CD Projekt Red")
            rockstar_developer = Developer.objects.get(name="Rockstar Games")

            playstation_4_platform = Platform.objects.get(name="PlayStation 4")
            xbox_one_platform = Platform.objects.get(name="Xbox One")
            pc_platform = Platform.objects.get(name="PC")

            best_game_badge = Badge.objects.get(name="Best Game")
            most_anticipated_badge = Badge.objects.get(name="Most Anticipated Game")

            games = [
                {
                    "title": "The Last of Us Part II",
                    "short_description": "A gripping story of survival in a post-apocalyptic world.",
                    "genres": [action_genre, adventure_genre],
                    "features": [stealth_feature, survival_feature],
                    "pegi_rating": 18,
                    "release_date": date(2020, 6, 19),
                    "long_description": "",
                    "publisher": [naughty_dog_publisher],
                    "developer": [naughty_dog_developer],
                    "platform": [playstation_4_platform],
                    "Badge": [best_game_badge],
                    "photo": "https://example.com/photo1.jpg",
                    "video": "https://example.com/video1.mp4",
                    "usd_price": 59.99
                },
                {
                    "title": "Cyberpunk 2077",
                    "short_description": "An open-world RPG set in a dystopian future.",
                    "genres": [rpg_genre, action_genre],
                    "features": [open_world_feature],
                    "pegi_rating": 18,
                    "release_date": date(2020, 12, 10),
                    "long_description": "",
                    "publisher": [cd_projekt_publisher],
                    "developer": [cd_projekt_developer],
                    "platform": [pc_platform, playstation_4_platform],
                    "Badge": [most_anticipated_badge],
                    "photo": "https://example.com/photo2.jpg",
                    "video": "https://example.com/video2.mp4",
                    "usd_price": 59.99
                },
                {
                    "title": "The Witcher 3: Wild Hunt",
                    "short_description": "A story-driven RPG set in a richly detailed fantasy world.",
                    "genres": [rpg_genre, adventure_genre],
                    "features": [open_world_feature],
                    "pegi_rating": 18,
                    "release_date": date(2015, 5, 19),
                    "long_description": "",
                    "publisher": [cd_projekt_publisher],
                    "developer": [cd_projekt_developer],
                    "platform": [pc_platform, playstation_4_platform],
                    "Badge": [best_game_badge],
                    "photo": "https://example.com/photo3.jpg",
                    "video": "https://example.com/video3.mp4",
                    "usd_price": 39.99
                },
                {
                    "title": "Red Dead Redemption 2",
                    "short_description": "A vast open-world game set in the American frontier.",
                    "genres": [action_genre, adventure_genre],
                    "features": [open_world_feature],
                    "pegi_rating": 18,
                    "release_date": date(2018, 10, 26),
                    "long_description": "",
                    "publisher": [rockstar_publisher],
                    "developer": [rockstar_developer],
                    "platform": [pc_platform, playstation_4_platform, xbox_one_platform],
                    "Badge": [best_game_badge],
                    "photo": "https://example.com/photo4.jpg",
                    "video": "https://example.com/video4.mp4",
                    "usd_price": 59.99
                },
                {
                    "title": "Fallout 4",
                    "short_description": "An open-world RPG set in a post-apocalyptic Boston.",
                    "genres": [rpg_genre],
                    "features": [open_world_feature],
                    "pegi_rating": 18,
                    "release_date": date(2015, 11, 10),
                    "long_description": "",
                    "publisher": [bethesda_publisher],
                    "developer": [bethesda_developer],
                    "platform": [pc_platform, playstation_4_platform, xbox_one_platform],
                    "Badge": [best_game_badge],
                    "photo": "https://example.com/photo5.jpg",
                    "video": "https://example.com/video5.mp4",
                    "usd_price": 49.99
                },
                {
                    "title": "Horizon Zero Dawn",
                    "short_description": "A post-apocalyptic open-world action RPG.",
                    "genres": [action_genre, adventure_genre],
                    "features": [open_world_feature],
                    "pegi_rating": 16,
                    "release_date": date(2017, 2, 28),
                    "long_description": "",
                    "publisher": [naughty_dog_publisher],
                    "developer": [naughty_dog_developer],
                    "platform": [playstation_4_platform],
                    "Badge": [best_game_badge],
                    "photo": "https://example.com/photo6.jpg",
                    "video": "https://example.com/video6.mp4",
                    "usd_price": 39.99
                },
                {
                    "title": "God of War",
                    "short_description": "An action-adventure game set in a world of Norse mythology.",
                    "genres": [action_genre, adventure_genre],
                    "features": [open_world_feature],
                    "pegi_rating": 18,
                    "release_date": date(2018, 4, 20),
                    "long_description": "",
                    "publisher": [naughty_dog_publisher],
                    "developer": [naughty_dog_developer],
                    "platform": [playstation_4_platform],
                    "Badge": [best_game_badge],
                    "photo": "https://example.com/photo7.jpg",
                    "video": "https://example.com/video7.mp4",
                    "usd_price": 49.99
                },
                {
                    "title": "Death Stranding",
                    "short_description": "An open-world action game with a unique story and gameplay.",
                    "genres": [action_genre, adventure_genre],
                    "features": [open_world_feature],
                    "pegi_rating": 18,
                    "release_date": date(2019, 11, 8),
                    "long_description": "",
                    "publisher": [naughty_dog_publisher],
                    "developer": [naughty_dog_developer],
                    "platform": [playstation_4_platform],
                    "Badge": [best_game_badge],
                    "photo": "https://example.com/photo8.jpg",
                    "video": "https://example.com/video8.mp4",
                    "usd_price": 59.99
                }

            ]

            for game_data in games:
                game = Game.objects.create(
                    title=game_data["title"],
                    short_description=game_data["short_description"],
                    pegi_rating=game_data["pegi_rating"],
                    release_date=game_data["release_date"],
                    long_description=game_data["long_description"],
                    photo=game_data["photo"],
                    video=game_data["video"],
                    usd_price=game_data["usd_price"]
                )
                game.genres.set(game_data["genres"])
                game.features.set(game_data["features"])
                game.publisher.set(game_data["publisher"])
                game.developer.set(game_data["developer"])
                game.platform.set(game_data["platform"])
                game.Badge.set(game_data["Badge"])

                self.stdout.write(f'Successfully added game: {game.title}')

        if SystemRequirement.objects.count():
            self.stdout.write(
                "There are `System Requirement` in the database, going to use them. "
            )
        else:
            game1 = Game.objects.get(title="The Last of Us Part II")
            game2 = Game.objects.get(title="Cyberpunk 2077")
            game3 = Game.objects.get(title="The Witcher 3: Wild Hunt")
            system_requirements_data = [
                SystemRequirement(game=game1, type="Minimum", os="Windows 10", processor="Intel Core i5-2500K",memory="8 GB RAM",
                                  storage="100 GB available space", graphics="NVIDIA GeForce GTX 780"),
                SystemRequirement(game=game1, type="Recommended", os="Windows 10", processor="Intel Core i7-4770K",
                                  memory="16 GB RAM", storage="100 GB available space", graphics="NVIDIA GeForce GTX 1060"),
                SystemRequirement(game=game2, type="Minimum", os="Windows 10", processor="Intel Core i5-3570K",
                                  memory="8 GB RAM", storage="70 GB available space", graphics="NVIDIA GeForce GTX 780"),
                SystemRequirement(game=game2, type="Recommended", os="Windows 10", processor="Intel Core i7-4790",
                                  memory="12 GB RAM", storage="70 GB available space", graphics="NVIDIA GeForce GTX 1060"),
                SystemRequirement(game=game3, type="Minimum", os="Windows 7", processor="Intel Core i5-2500K",
                                  memory="6 GB RAM", storage="35 GB available space", graphics="NVIDIA GeForce GTX 660"),
                SystemRequirement(game=game3, type="Recommended", os="Windows 10", processor="Intel Core i7-3770",
                                  memory="8 GB RAM", storage="35 GB available space", graphics="NVIDIA GeForce GTX 770")
            ]
            SystemRequirement.objects.bulk_create(system_requirements_data)