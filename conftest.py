import pytest

from fixtures.factories import (
    GenreFactory, PublisherFactory, BadgeFactory, DeveloperFactory, PlatformFactory, FeatureFactory, GameFactory,
    SystemRequirementFactory
)


# Factories
@pytest.fixture(scope='session')
def genre_factory():
    return GenreFactory


@pytest.fixture(scope='session')
def publisher_factory():
    return PublisherFactory


@pytest.fixture(scope='session')
def badge_factory():
    return BadgeFactory


@pytest.fixture(scope='session')
def developer_factory():
    return DeveloperFactory


@pytest.fixture(scope='session')
def platform_factory():
    return PlatformFactory


@pytest.fixture(scope='session')
def feature_factory():
    return FeatureFactory


@pytest.fixture(scope='session')
def game_factory():
    return GameFactory

@pytest.fixture(scope='session')
def system_requirement_factory():
    return SystemRequirementFactory


@pytest.fixture
def genres(genre_factory):
    return genre_factory.create_batch(3)


@pytest.fixture
def genre(genre_factory):
    return genre_factory.create()


@pytest.fixture
def publishers(publisher_factory):
    return publisher_factory.create_batch(3)


@pytest.fixture
def publisher(publisher_factory):
    return publisher_factory.create()


@pytest.fixture
def developers(developer_factory):
    return developer_factory.create_batch(3)


@pytest.fixture
def developer(developer_factory):
    return developer_factory.create()


@pytest.fixture
def platforms(platform_factory):
    return platform_factory.create_batch(3)


@pytest.fixture
def platform(platform_factory):
    return platform_factory.create()


@pytest.fixture
def features(feature_factory):
    return feature_factory.create_batch(3)


@pytest.fixture
def feature(feature_factory):
    return feature_factory.create()


@pytest.fixture
def badges(badges_factory):
    return badges_factory.create_batch(3)


@pytest.fixture
def badge(badges_factory):
    return badges_factory.create()
