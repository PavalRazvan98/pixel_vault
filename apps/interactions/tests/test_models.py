import pytest


@pytest.mark.django_db
def test_sessions_str(session):
    assert str(session) == f"{session.user_id} played {session.game_id} for {session.time_play}"
