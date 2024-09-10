import factory

from apps.games.choices import PEGIOptions, TypeOptions


class GameFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'games.Game'

    title = factory.Faker('sentence')
    short_description = factory.Faker('paragraph')
    pegi_rating = factory.Faker('random_element', elements=PEGIOptions)
    release_date = factory.Faker('date_this_decade')
    long_description = factory.Faker('paragraphs')
    photo = factory.Faker('url')
    video = factory.Faker('url')
    usd_price = factory.Faker('pyfloat')

    @factory.post_generation
    def genres(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        self.genres.add(*extracted)

    @factory.post_generation
    def features(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        self.features.add(*extracted)

    @factory.post_generation
    def publishers(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        self.publishers.add(*extracted)

    @factory.post_generation
    def developers(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        self.developers.add(*extracted)

    @factory.post_generation
    def platforms(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        self.platforms.add(*extracted)

    @factory.post_generation
    def badges(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        self.badges.add(*extracted)


class SystemRequirementFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'games.SystemRequirement'

    game = factory.SubFactory(GameFactory)
    type = factory.Faker('random_element', elements=TypeOptions)
    os = factory.Faker('word')
    processor = factory.Faker('word')
    memory = factory.Faker('word')
    storage = factory.Faker('word')
    graphics = factory.Faker('word')
