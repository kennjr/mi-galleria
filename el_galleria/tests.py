import os
from django.test import TestCase


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'galleria.settings')
import django
django.setup()

from .models import Location, Category, Galleria


# Create your tests here.
class LocationTestsClass(TestCase):
    # set up method
    def setUp(self):
        self.location = Location.objects.create(name="Kilimani", address="5 Montie St")

    # testing instance
    def test_instance(self):
        location = self.location
        self.assertEqual(self.location, location)

    # testing save method
    def test_save_location_method(self):
        self.location.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)

    def test_delete_location_method(self):
        self.location.save_location()
        original_len = Location.objects.all()
        print(f'the locations are{len(original_len)}')
        Location.delete_location(self.location.id)
        locations = Location.objects.all()
        print(f'the locations are{len(locations)}')
        self.assertTrue((len(locations)) == (len(original_len) - 1))


class CategoryTestsClass(TestCase):
    # set up method
    def setUp(self):
        self.category = Category.objects.create(category_str="traveller", slug="travellerr")

    # testing instance
    def test_instance(self):
        category = self.category
        self.assertEqual(self.category, category)

    # testing save method
    def test_save_category_method(self):
        self.category.save_category()
        location = Category.objects.all()
        self.assertTrue(len(location) > 0)

    def test_delete_category_method(self):
        self.category.save_category()
        original_len = Category.objects.all()
        print(f'the categorys are{len(original_len)}')
        Category.delete_category(self.category.id)
        categorys = Category.objects.all()
        print(f'the categorys are{len(categorys)}')
        self.assertTrue((len(categorys)) == (len(original_len) - 1))


