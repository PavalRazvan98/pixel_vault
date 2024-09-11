import pytest
from django.contrib.auth import get_user_model
from django.core.management import call_command

from apps.feedback.models import Rating
from apps.games.models import Game, SystemRequirement
from apps.interactions.models import Session
from apps.misc.models import Badge, Feature, Genre, Platform, Developer, Publisher

User = get_user_model()

@pytest.mark.django_db
def test_populate_database():
    assert Game.objects.count() == 0
    assert SystemRequirement.objects.count() == 0
    assert Rating.objects.count() == 0
    assert Session.objects.count() == 0
    assert Badge.objects.count() == 0
    assert Feature.objects.count() == 0
    assert Genre.objects.count() == 0
    assert Platform.objects.count() == 0
    assert Developer.objects.count() == 0
    assert Publisher.objects.count() == 0
    assert User.objects.count() == 0

    call_command("populate_database")

    assert Game.objects.count() == 8
    assert SystemRequirement.objects.count() == 6
    assert Rating.objects.count() != 0
    assert Session.objects.count() != 0
    assert Badge.objects.count() == 7
    assert Feature.objects.count() == 10
    assert Platform.objects.count() == 7
    assert Developer.objects.count() == 8
    assert Publisher.objects.count() == 12
    assert Genre.objects.count() == 9
    assert User.objects.filter(is_superuser=False, is_staff=False).count() == 15



@pytest.mark.django_db
def test_populate_database__skip_publisher(publishers):
    call_command("populate_database")
    assert Publisher.objects.count() == 3


@pytest.mark.django_db
def test_populate_database__skip_genre(genres):
    call_command("populate_database")
    assert Genre.objects.count() == 3


@pytest.mark.django_db
def test_populate_database__skip_developer(developers):
    call_command("populate_database")
    assert Developer.objects.count() == 3


@pytest.mark.django_db
def test_populate_database__skip_platform(platforms):
    call_command("populate_database")
    assert Platform.objects.count() == 3


@pytest.mark.django_db
def test_populate_database__skip_feature(features):
    call_command("populate_database")
    assert Feature.objects.count() == 3


@pytest.mark.django_db
def test_populate_database__skip_badges(badges):
    call_command("populate_database")
    assert Badge.objects.count() == 3


@pytest.mark.django_db
def test_populate_database__skip_game(games):
    call_command("populate_database")
    assert Game.objects.count() == 3


@pytest.mark.django_db
def test_populate_database__skip_system_requirement(system_requirements):
    call_command("populate_database")
    assert SystemRequirement.objects.count() == 3


@pytest.mark.django_db
def test_populate_database__skip_rating(ratings):
    call_command("populate_database")
    assert Rating.objects.count() == 3


@pytest.mark.django_db
def test_populate_database__skip_session(sessions):
    call_command("populate_database")
    assert Session.objects.count() == 3
