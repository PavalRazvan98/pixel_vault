import pytest

from fixtures.factories import (
    BadgeFactory,
    DeveloperFactory,
    FeatureFactory,
    GameFactory,
    GenreFactory,
    PlatformFactory,
    PublisherFactory,
    RatingFactory,
    SessionFactory,
    SystemRequirementFactory,
    MediaFactory,
)


@pytest.fixture(scope="session")
def genre_factory():
    return GenreFactory


@pytest.fixture(scope="session")
def publisher_factory():
    return PublisherFactory


@pytest.fixture(scope="session")
def badge_factory():
    return BadgeFactory


@pytest.fixture(scope="session")
def developer_factory():
    return DeveloperFactory


@pytest.fixture(scope="session")
def platform_factory():
    return PlatformFactory


@pytest.fixture(scope="session")
def feature_factory():
    return FeatureFactory


@pytest.fixture(scope="session")
def game_factory():
    return GameFactory


@pytest.fixture(scope="session")
def system_requirement_factory():
    return SystemRequirementFactory


@pytest.fixture(scope="session")
def media_factory():
    return MediaFactory


@pytest.fixture(scope="session")
def rating_factory():
    return RatingFactory


@pytest.fixture(scope="session")
def session_factory():
    return SessionFactory


# ? ?
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
def badges(badge_factory):
    return badge_factory.create_batch(3)


@pytest.fixture
def badge(badge_factory):
    return badge_factory.create()


@pytest.fixture
def game(game_factory):
    return game_factory.create()


@pytest.fixture
def games(game_factory):
    return game_factory.create_batch(3)


@pytest.fixture
def media(media_factory):
    return media_factory.create()


@pytest.fixture
def medias(media_factory):
    return media_factory.create_batch(3)


@pytest.fixture
def system_requirement(system_requirement_factory):
    return system_requirement_factory.create()


@pytest.fixture
def system_requirements(system_requirement_factory):
    return system_requirement_factory.create_batch(3)


@pytest.fixture
def rating(rating_factory):
    return rating_factory.create()


@pytest.fixture
def ratings(rating_factory):
    return rating_factory.create_batch(3)


@pytest.fixture
def session(session_factory):
    return session_factory.create()


@pytest.fixture
def sessions(session_factory):
    return session_factory.create_batch(3)
