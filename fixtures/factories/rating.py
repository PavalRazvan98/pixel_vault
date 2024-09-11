import factory

from fixtures.factories import GameFactory
from fixtures.factories.core import UserFactory


class RatingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'feedback.Rating'

    game = factory.SubFactory(GameFactory)
    user = factory.SubFactory(UserFactory)
    content = factory.Faker('sentence')
    score = factory.Faker('pyint')
    submitted_review = factory.Faker('date_this_decade')