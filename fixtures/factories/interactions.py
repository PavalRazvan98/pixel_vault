from datetime import timedelta
from random import randint
import factory

from fixtures.factories import GameFactory
from fixtures.factories.core import UserFactory


class SessionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'interactions.Session'

    game = factory.SubFactory(GameFactory)
    user = factory.SubFactory(UserFactory)
    last_play = factory.Faker('date_this_decade')
    time_play = factory.LazyFunction(lambda: timedelta(minutes=randint(1, 500)))
    ip_address = factory.Faker("ipv4")
