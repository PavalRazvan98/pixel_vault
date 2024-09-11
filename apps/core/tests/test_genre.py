import pytest

from apps.games.models import Game


@pytest.mark.django_db
def test_genre(genre_factory, publisher_factory, badge_factory, game_factory, system_requirement_factory):
    genre_factory.create()
    p1 = publisher_factory.create(name="123")
    p2 = publisher_factory.create()

    assert p1.name == "123"
    assert p1.name != p2.name

    g = game_factory.create(publishers=[p1, p2])
    assert p1 in g.publishers.all()
    assert p2 in g.publishers.all()

    assert Game.objects.count() == 1
    system_requirement_factory.create()  # this is going to create a new game
    assert Game.objects.count() == 2

    assert Game.objects.count() == 2
    system_requirement_factory.create(game=g)  # this is NOT going to create a new game
    assert Game.objects.count() == 2
