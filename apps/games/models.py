from django.db import models

from apps.games.choices import TypeOptions, PEGIOptions


class Game(models.Model):

    title = models.CharField(max_length=150)
    short_description = models.CharField(max_length=200)
    genres = models.ManyToManyField("misc.Genre")
    features = models.ManyToManyField("misc.Feature")
    pegi_rating = models.IntegerField(choices=PEGIOptions, null=True)
    release_date = models.DateField()
    long_description = models.TextField(null=True, blank=True)
    publisher = models.ManyToManyField("misc.Publisher")
    developer = models.ManyToManyField("misc.Developer")
    platform = models.ManyToManyField("misc.Platform")
    badges = models.ManyToManyField("misc.Badge")
    photo = models.URLField(max_length=1000, null=True, blank=True)
    video = models.URLField(max_length=1000, null=True, blank=True)
    usd_price = models.FloatField()

    def __str__(self):
        return self.title

    def photo_display(self):
        return self.photo if self.photo is not None else "https://demofree.sirv.com/nope-not-here.jpg"

    def video_display(self):
        return  self.video if self.video is not None else "https://i.ytimg.com/vi/UH1ThWZ9hXU/hqdefault.jpg"


class SystemRequirement(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=TypeOptions)
    os = models.CharField(max_length=100)
    processor = models.CharField(max_length=100)
    memory = models.CharField(max_length=100)
    storage = models.CharField(max_length=100)
    graphics = models.CharField(max_length=1500)

    class Meta:
        unique_together = ("game", "type", "os")