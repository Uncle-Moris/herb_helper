from herbs.tests.factory import FlavorFactory
from django.test import TestCase

from herbs.models.models import Flavor


class FlavorTestCase(TestCase):
    def test_flavor_creation(self):
        flavor = FlavorFactory.create()
        self.assertIsInstance(flavor, Flavor)
        self.assertIsNotNone(flavor.name)
