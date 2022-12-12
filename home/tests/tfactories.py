import factory
from faker import Faker
from home.models import Game, Team, Player

fake = Faker()

class GameFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Game

    
    home_team: str = fake.country()
    away_team: str = fake.country()
    home_score: int = fake.pyint(min_value=0, max_value=10)
    away_score: int = fake.pyint(min_value=0, max_value=10)
    mom: str = fake.name()


class TeamFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Team
    
    name = fake.company()
    city = fake.city()

class PlayerFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Player
    
    name = fake.name()
    age = fake.pyint(min_value=15, max_value=40)
    team = factory.SubFactory(TeamFactory)
