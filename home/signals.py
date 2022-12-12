
from django.db.models.signals import pre_save
from home.models import Game
from django.dispatch import receiver

@receiver(signal=pre_save, sender=Game)
def game_save_pre_handler(*args, **kwargs):
    """a signal function that determines the game result
    """
    if kwargs["instance"].home_score > kwargs["instance"].away_score:
        kwargs["instance"].result = "H"
    elif kwargs["instance"].home_score < kwargs["instance"].away_score:
        kwargs["instance"].result = "A"
    else:
        kwargs["instance"].result = "D"

pre_save.connect(receiver=game_save_pre_handler, sender=Game)