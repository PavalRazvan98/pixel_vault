from django.views import generic

from apps.games.models import Game


class Homepage(generic.ListView):
    template_name = 'pixel_vault/homepage.html'
    context_object_name = 'all_games'
    queryset = Game.objects.all()


class DetailViewGame(generic.DetailView):
    model = Game
    template_name = 'pixel_vault/game_details.html'
    context_object_name = 'game'
