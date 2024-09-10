import factory
import pytest

from apps.misc.models import Publisher, Developer, Platform, Feature, Badge
from fixtures.factories import GenreFactory
from fixtures.factories.misc import PublisherFactory, BadgeFactory


@pytest.fixture(scope='session')
def genre_factory():
    return GenreFactory


@pytest.fixture(scope='session')
def publisher_factory():
    return PublisherFactory

@pytest.fixture(scope='session')
def badge_factory():
    return BadgeFactory


@pytest.fixture
def genres(genre_factory):
    return genre_factory.create_batch(3)


@pytest.fixture
def genre(genre_factory):
    return genre_factory.create()


# Publisher
@pytest.fixture(scope='session')
def publisher_factory():
    class PublisherFactory(factory.django.DjangoModelFactory):
        class Meta:
            model = Publisher

    return PublisherFactory


@pytest.fixture
def publishers(publisher_factory):
    return publisher_factory.create_batch(3)


@pytest.fixture
def publisher(publisher_factory):
    return publisher_factory.create()


# Developer
@pytest.fixture(scope='session')
def developer_factory():
    class DeveloperFactory(factory.django.DjangoModelFactory):
        class Meta:
            model = Developer

    return DeveloperFactory


@pytest.fixture
def developers(developer_factory):
    return developer_factory.create_batch(3)


@pytest.fixture
def developer(developer_factory):
    return developer_factory.create()


# Platform
@pytest.fixture(scope='session')
def platform_factory():
    class PlatformFactory(factory.django.DjangoModelFactory):
        class Meta:
            model = Platform

    return PlatformFactory


@pytest.fixture
def platforms(platform_factory):
    return platform_factory.create_batch(3)


@pytest.fixture
def platform(platform_factory):
    return platform_factory.create()


# Feature
@pytest.fixture(scope="session")
def feature_factory():
    class FeatureFactory(factory.django.DjangoModelFactory):
        class Meta:
            model = Feature

    return FeatureFactory


@pytest.fixture
def features(feature_factory):
    return feature_factory.create_batch(3)


@pytest.fixture
def feature(feature_factory):
    return feature_factory.create()


# Badge
@pytest.fixture(scope="session")
def badges_factory():
    class BadgesFactory(factory.django.DjangoModelFactory):
        class Meta:
            model = Badge

    return BadgesFactory


@pytest.fixture
def Badge(badges_factory):
    return badges_factory.create_batch(3)


@pytest.fixture
def badge(badges_factory):
    return badges_factory.create()

# Games
# @pytest.fixture(scope="session")
# def games_factory():
#     class GamesFactory(factory.django.DjangoModelFactory):
#         class Meta:
#             model = Game
#         release_date = factory.Faker('date')
#
#     return GamesFactory
#
#
# @pytest.fixture
# def games(games_factory):
#     return games_factory.create_batch(3)
#
#
# @pytest.fixture
# def game(games_factory):
#     return games_factory.create()
#
#
# # Session
# @pytest.fixture(scope="session")
# def session_factory():
#     class SessionFactory(factory.django.DjangoModelFactory):
#         class Meta:
#             model = Session
#
#         time_play = factory.Faker('time_delta')
#         ip_address = factory.Faker('ipv4')
#
#     return SessionFactory
#
#
# @pytest.fixture
# def sessions(session_factory, games):
#     return session_factory.create_batch(3)
#
#
# @pytest.fixture
# def session(session_factory, game):
#     return session_factory.create()
