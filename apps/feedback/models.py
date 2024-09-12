from datetime import datetime

from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

User = get_user_model()


class Rating(models.Model):
    game = models.ForeignKey("games.Game", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.CharField(max_length=200)
    score = models.IntegerField(null=True, validators=[MaxValueValidator(5), MinValueValidator(1)])
    submitted_review = models.DateField(default=datetime.now)

    class Meta:
        unique_together = ("game", "user")

    def __str__(self):
        return f"{self.game} rated by {self.user} with score {self.score}/5"
