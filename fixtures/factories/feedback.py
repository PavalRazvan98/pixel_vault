import factory

from fixtures.factories import GameFactory
from fixtures.factories.core import UserFactory


class RatingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'feedback.Rating'

    game = factory.SubFactory(GameFactory)
    user = factory.SubFactory(UserFactory)
    content = factory.Faker('sentence')
    score = factory.Faker('pyint', min_value=0, max_value=5)
    submitted_review = factory.Faker('date_this_decade')