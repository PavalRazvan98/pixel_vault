from django.db.models import Avg, Sum
from django.views import generic
from django.views.generic import TemplateView

from apps.feedback.models import Rating
from apps.games.models import Game


class Homepage(generic.ListView):
    template_name = "pixel_vault/homepage.html"
    context_object_name = "all_games"
    queryset = Game.objects.all()


class DetailViewGame(generic.DetailView):
    model = Game
    template_name = "pixel_vault/game_details.html"
    context_object_name = "game"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Ratings"] = Rating.objects.filter(game=self.object)
        return context


class MostAppreciatedGamesView(generic.ListView):
    model = Game
    template_name = "pixel_vault/most_appreciated_games.html"
    context_object_name = "games"

    def get_queryset(self):
        return Game.objects.annotate(average_score=Avg("rating__score")).order_by("-average_score")


class MostPlayedGamesView(TemplateView):
    template_name = "pixel_vault/most_played_games.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        most_played_games = (
            Game.objects.annotate(total_played_time=Sum("session__time_play"))
            .filter(total_played_time__isnull=False)
            .order_by("-total_played_time")
        )

        for game in most_played_games:
            game.total_played_time_formatted = self.format_play_time(game.total_played_time)

        context["games"] = most_played_games
        return context

    def format_play_time(self, play_time):
        days = play_time.days
        hours, remainder = divmod(play_time.seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        return f"{days}d {hours}h {minutes}m"
