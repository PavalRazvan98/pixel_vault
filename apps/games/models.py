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
    publishers = models.ManyToManyField("misc.Publisher")
    developers = models.ManyToManyField("misc.Developer")
    platforms = models.ManyToManyField("misc.Platform")
    badges = models.ManyToManyField("misc.Badge")
    photo = models.URLField(max_length=1000, null=True, blank=True)
    video = models.URLField(max_length=1000, null=True, blank=True)
    usd_price = models.FloatField()

    def __str__(self):
        return f'{self.title} ({self.release_year})'

    def photo_display(self):
        return self.photo if self.photo is not None else "https://demofree.sirv.com/nope-not-here.jpg"

    def video_display(self):
        return  self.video if self.video is not None else "https://i.ytimg.com/vi/UH1ThWZ9hXU/hqdefault.jpg"

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

    # TODO: Create two properties for this, memory & storage, which will return a string
    #   e.g. if storage_mb is between 0 and 1023 return a string like 240 MB,
    #   if it's bigger than 1023, return it like this 1.7 GB. Same for memory

    class Meta:
        unique_together = ("game", "type", "os")

    @property
    def memory_display(self):
        if self.memory_mb < 1024:
            return f"{self.memory_mb} MB"
        else:
            return f"{self.memory_mb / 1024} GB"

    @property
    def storage_display(self):
        if self.storage_mb < 1024:
            return f"{self.storage_mb} MB"
        else:
            return f"{self.storage_mb / 1024} GB"
