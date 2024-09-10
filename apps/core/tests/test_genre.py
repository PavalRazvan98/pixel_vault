import pytest


@pytest.mark.django_db
def test_genre(genre_factory, publisher_factory, badge_factory):
    publisher_factory.create()
    pass
