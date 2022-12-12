import pytest
from home.models import Game

# @pytest.fixture
# def new_game_factory(db):
#     def create_new_game_record(home_team: str = "England", 
#                             away_team: str = "France", 
#                             home_score: int = 1, 
#                             away_score: int = 2, 
#                             mom: str = "Harry Maguire"):
#         data = {"home_team":home_team,"away_team":away_team,"home_score":home_score, "away_score":away_score, "mom":mom}
#         g = Game(**data)
#         g.save()
#         return g
#     return create_new_game_record   

# @pytest.fixture
# def new_game_default(db, new_game_factory):
#     return new_game_factory()

# @pytest.fixture
# def new_game(db, new_game_factory):
#     return new_game_factory("Crotia", "Brazil", 1, 1, "Dominik Livakovic")
from pytest_factoryboy import register
from home.tests.tfactories import GameFactory

register(GameFactory) #game_factory

@pytest.fixture
def new_game_record(db, game_factory):
    game = game_factory.build()
    return game

from home.tests.tfactories import PlayerFactory, TeamFactory

register(PlayerFactory)
register(TeamFactory)