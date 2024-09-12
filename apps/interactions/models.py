from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Session(models.Model):
    game = models.ForeignKey("games.Game", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    last_play = models.DateField(auto_now_add=True)
    time_play = models.DurationField()
    ip_address = models.GenericIPAddressField()

    class Meta:
        unique_together = ("game", "user")

    def __str__(self):
        return f"{self.user} playd {self.game} for {self.time_play}"
