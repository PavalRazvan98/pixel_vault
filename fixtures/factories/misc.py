import factory

from apps.misc.choices import DeveloperEntity, NationalityOptions


class PublisherFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "misc.Publisher"
        django_get_or_create = ("name",)

    name = factory.Faker("word")
    nationality = factory.Faker("random_element", elements=NationalityOptions)


class DeveloperFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "misc.Developer"
        django_get_or_create = ("name",)

    name = factory.Faker("word")
    nationality = factory.Faker("random_element", elements=NationalityOptions)
    entity = factory.Faker("random_element", elements=DeveloperEntity)


class PlatformFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "misc.Platform"
        django_get_or_create = ("name",)

    name = factory.Faker("word")
    logo = factory.Faker("url")


class GenreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "misc.Genre"
        django_get_or_create = ("name",)

    name = factory.Faker("word")


class FeatureFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "misc.Feature"
        django_get_or_create = ("name",)

    name = factory.Faker("word")


class BadgeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "misc.Badge"
        django_get_or_create = ("name",)

    name = factory.Faker("word")
