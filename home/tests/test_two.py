import pytest
from home.models import Game

@pytest.mark.skip
@pytest.mark.parametrize(
    "home_team , away_team , home_score , away_score , mom",
    [
        ("Japan", "Spain" , 2, 1, "Ao Tanaka"),
        ("Costa Rica", "Germany" ,2 , 4, "Kai Havertz"),
    ],
)
def test_game_instance(db, game_factory, home_team, away_team, home_score, away_score, mom):
    game = game_factory(
        home_team=home_team,
        away_team=away_team,
        home_score=home_score,
        away_score=away_score,
        mom=mom
    )
    count = Game.objects.all().count()
    assert count == 1
