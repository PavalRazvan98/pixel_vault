from django.db import models


class TypeOptions(models.TextChoices):
    Minimum = "Minimum"
    Recommended = "Recommended"


class PEGIOptions(models.IntegerChoices):
    P_3 = 3, "PEGI 3"
    P_7 = 7, "PEGI 7"
    P_12 = 12, "PEGI 12"
    P_16 = 16, "PEGI 16"
    P_18 = 18, "PEGI 18"


class MediaOptions(models.TextChoices):
    photo = "photo"
    video = "video"
    documents = "documents"
