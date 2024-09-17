import pytest


@pytest.mark.django_db
def test_rating_str(rating):
    assert str(rating) == f"{rating.game_id} rated by {rating.user_id} with score {rating.score}/5"
