from django.db import models

from apps.games.choices import PEGIOptions, TypeOptions


class Game(models.Model):
    title = models.CharField(max_length=150)
    short_description = models.CharField(max_length=200)
    genres = models.ManyToManyField("misc.Genre")
    features = models.ManyToManyField("misc.Feature")
    pegi_rating = models.IntegerField(choices=PEGIOptions, null=True)
    release_date = models.DateField()
    long_description = models.TextField(blank=True)
    publishers = models.ManyToManyField("misc.Publisher")
    developers = models.ManyToManyField("misc.Developer")
    platforms = models.ManyToManyField("misc.Platform")
    badges = models.ManyToManyField("misc.Badge")
    photo = models.URLField(max_length=1000, blank=True)
    video = models.URLField(max_length=1000, blank=True)
    usd_price = models.FloatField()

    def __str__(self):
        return f"{self.title} ({self.release_year})"

    def photo_display(self):
        return self.photo if self.photo is not None else "https://demofree.sirv.com/nope-not-here.jpg"

    def video_display(self):
        return self.video if self.video is not None else "https://i.ytimg.com/vi/UH1ThWZ9hXU/hqdefault.jpg"

    @property
    def release_year(self):
        return self.release_date.year


class SystemRequirement(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=TypeOptions)
    os = models.CharField(max_length=100)
    processor = models.CharField(max_length=100)
    memory_mb = models.IntegerField()
    storage_mb = models.IntegerField()
    graphics = models.CharField(max_length=1500)

    class Meta:
        unique_together = ("game", "type", "os")

    def __str__(self):
        return f"{self.game} {self.type} run on {self.os}"

    @property
    def memory(self):
        mb = 1024
        if self.memory_mb is None or self.memory_mb == 0:
            return "None"
        if self.memory_mb < mb:
            return f"{self.memory_mb} MB"
        return f"{self.memory_mb / mb} GB"

    @property
    def storage(self):
        mb = 1024
        if self.storage_mb is None or self.storage_mb == 0:
            return "None"
        if self.storage_mb < mb:
            return f"{self.storage_mb} MB"
        return f"{self.storage_mb / mb} GB"
