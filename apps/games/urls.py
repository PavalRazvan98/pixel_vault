from django.urls import path

from . import views

urlpatterns = [
    path("homepage/", views.Homepage.as_view(), name="homepage"),
    path("game/<int:pk>/", views.DetailViewGame.as_view(), name="game-details"),
    path('most-appreciated/', views.MostAppreciatedGamesView.as_view(), name='most-appreciated'),
    path("most-played/", views.MostPlayedGamesView.as_view(), name='most-played'),
]
