from django.urls import path

from . import views

urlpatterns = [
    path("homepage/", views.Homepage.as_view(), name="homepage"),
    path("game/<int:pk>/", views.DetailViewGame.as_view(), name="game-details"),
]
