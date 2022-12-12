from django.forms import ModelForm
from home.models import Game

class GameForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(GameForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Game
        fields = ['home_team', 'away_team', 'home_score', 'away_score', 'mom']

