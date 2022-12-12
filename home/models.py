from django.db import models

class Game(models.Model):

    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    home_score = models.IntegerField(blank=False)
    away_score = models.IntegerField(blank=False)
    result = models.CharField(max_length=1)
    mom = models.CharField(max_length=100)

class Team(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.RESTRICT)

    def __str__(self):
        return self.name + " - " + self.team