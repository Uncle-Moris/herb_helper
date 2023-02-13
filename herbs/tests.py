from django.test import TestCase

from .models.models import Herb, Flavor


class HerbTestCase(TestCase):
    def setUp(self):
        Flavor.objects.create(name="Sour", )