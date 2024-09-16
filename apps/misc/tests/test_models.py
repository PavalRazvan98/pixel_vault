import pytest

from apps.misc.models import Publisher


@pytest.mark.django_db
def test_publisher_str(publisher):
    assert str(publisher) == publisher.name


@pytest.mark.django_db
def test_developer_str(developer):
    assert str(developer) == developer.name
    
  
@pytest.mark.django_db
def test_badge_str(badge):
    assert str(badge) == badge.name
    
    
@pytest.mark.django_db
def test_platform_str(platform):
    assert str(platform) == platform.name
    
        
@pytest.mark.django_db
def test_genre_str(genre):
    assert str(genre) == genre.name
    

@pytest.mark.django_db
def test_feature_str(feature):
    assert str(feature) == feature.name

    