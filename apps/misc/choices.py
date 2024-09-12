from django.db import models


class NationalityOptions(models.TextChoices):
    USA = "Usa"
    France = "France"
    Germany = "Germany"
    Japan = "Japan"
    China = "China"
    Uk = "Uk"
    Russian = "Russian"
    Poland = "Poland"
    Canada = "Canada"
    Unknown = "Unknown"


class DeveloperEntity(models.TextChoices):
    Person = "Person"
    Company = "Company"
    Unknown = "Unknown"
