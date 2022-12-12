import pytest
from home.models import Game

@pytest.mark.skip
def test_pass():
    assert True == True

@pytest.mark.skip
def test_fail():
    assert True == False

@pytest.mark.skip
@pytest.mark.django_db
def test_create():
    pre_count = Game.objects.all().count()
    data = {"home_team":"England","away_team":"France","home_score":1, "away_score":2, "mom":"Harry Maguire"}
    g = Game(**data)
    g.save()
    count = Game.objects.all().count()
    assert count - pre_count == 1

@pytest.mark.skip
@pytest.fixture()
def game(db):
    data = {"home_team":"England","away_team":"France","home_score":1, "away_score":2, "mom":"Harry Maguire"}
    g = Game(**data)
    g.save()
    return g

@pytest.mark.skip
@pytest.mark.django_db
def test_update_record(game):
    game.mom = "Kylian Mbappe"
    assert game.mom == "Kylian Mbappe"

@pytest.mark.skip
def test_new_game_default(new_game_default):
    assert new_game_default.home_team == "England"

@pytest.mark.skip
def test_new_game(new_game):
    assert new_game.home_team == "England"
    
@pytest.mark.skip
def test_create_object(game_factory):
    g = game_factory.build()
    assert True

@pytest.mark.skip
@pytest.mark.django_db
def test_save_object(game_factory):
    init_count = Game.objects.all().count()
    g = game_factory.create()
    last_count = Game.objects.all().count()
    assert last_count - init_count == 1

@pytest.mark.skip
def test_player(player_factory):
    player = player_factory.build()
    assert True