from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from home.forms import GameForm
from home.models import Game
class HomeView(View):

    def get(self, request):
        form = GameForm()
        games = Game.objects.all()
        return render(request, './templates/home.html', {'form': form, 'games': games})

    def post(self, request):
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')

class DetailView(View):

    def get(self, request, pk):
        game = get_object_or_404(Game, pk=pk)
        return render(request, './templates/detail.html', {'game': game})