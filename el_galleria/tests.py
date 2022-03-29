import os
from django.test import TestCase


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'galleria.settings')
import django
django.setup()

from .models import Location, Category, Galleria

# Create your tests here.

class LocationTestClass(TestCase):
    # set up method
    def setUp(self):
        self.location = Location.objects.create(name="Kilimani", address="5 Montie St")

    # testing instance
    def test_instance(self):
        location = self.location
        self.assertEqual(self.location, location)

    # testing save method
    def test_save_method(self):
        self.location.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)

    def test_delete_method(self):
        self.location.save_location()
        original_len = Location.objects.all()
        print(f'the locations are{len(original_len)}')
        Location.delete_location(self.location.id)
        locations = Location.objects.all()
        print(f'the locations are{len(locations)}')
        self.assertTrue((len(locations)) == (len(original_len) - 1))

