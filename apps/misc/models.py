
from django.db import models

from apps.misc.choices import NationalityOptions, DeveloperEntity


class Publisher(models.Model):
    name = models.CharField(max_length=200)
    nationality = models.CharField(max_length=50, choices=NationalityOptions, default=NationalityOptions.Unknown)
    still_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Developer(models.Model):
    name = models.CharField(max_length=200)
    nationality = models.CharField(max_length=50, choices=NationalityOptions, default=NationalityOptions.Unknown)
    entity = models.CharField(max_length=50, choices=DeveloperEntity,default=DeveloperEntity.Unknown)
    still_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Platform(models.Model):
    name = models.CharField(max_length=100)
    logo = models.URLField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Feature(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Badges(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

