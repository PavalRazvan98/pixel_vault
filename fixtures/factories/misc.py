import factory
from factory.base import T

from apps.misc.choices import NationalityOptions, DeveloperEntity


class PublisherFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'misc.Publisher'
        django_get_or_create = ('name',)

    name = factory.Faker('word')
    # name = models.CharField(max_length=200, unique=True)
    # name = 'd/asdasdas'
    # nationality = factory.Faker('random_element', elements=NationalityOptions.choices)

    @classmethod
    def create(cls, **kwargs) -> T:
        return super().create(**kwargs)


class DeveloperFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'misc.Developer'
        django_get_or_create = ('name',)

    name = factory.Faker('word')
    nationality = factory.Faker('random_element', elements=NationalityOptions.choices)
    entity = factory.Faker('random_element', elements=DeveloperEntity.choices)


class PlatformFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'misc.Platform'
        django_get_or_create = ('name',)

    name = factory.Faker('word')
    logo = factory.Faker('url')


class GenreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'misc.Genre'
        django_get_or_create = ('name',)

    name = factory.Faker('word')


class FeatureFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'misc.Feature'
        django_get_or_create = ('name',)

    name = factory.Faker('word')


class BadgeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'misc.Badge'
        django_get_or_create = ('name',)

    name = factory.Faker('word')
