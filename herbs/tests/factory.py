from herbs.models.models import Flavor
from factory.django import DjangoModelFactory, DjangoOptions
from factory import LazyFunction
from faker import Faker

fake = Faker()


class FlavorFactory(DjangoModelFactory):
    class Meta:
        model = Flavor

    name = LazyFunction(lambda: fake.name())
