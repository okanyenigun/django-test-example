import pytest
from mixer.backend.django import mixer

@pytest.mark.django_db
class TestModel:

    def test_game_result(self):
        g = mixer.blend('home.Game',home_score=1, away_score=2)
        assert g.result == 'A'