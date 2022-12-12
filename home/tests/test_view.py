import pytest
from mixer.backend.django import mixer
from django.test import RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from home.views import DetailView

@pytest.mark.django_db
class TestView:

    def test_game_detail_view(self):
        mixer.blend('home.Game',home_score=1, away_score=2)
        path =reverse('detail', kwargs={'pk':1})
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)
        D = DetailView()
        response = D.get(request, 1)
        assert response.status_code == 200