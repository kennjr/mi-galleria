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


class GalleriaTestsClass(TestCase):
    # set up method
    def setUp(self):
        self.test_location = Location.objects.create(name='Kileleshwa', address="1 Kieni Rd")
        # self.test_location.save_location()

        # creating a new category
        self.test_category = Category.objects.create(category_str='test category', slug="test-category")
        # self.test_category.save_category()

        self.gallery_img = Galleria(description='The mountains', img_url='galleria_imgs/hobbies_7.jpg',
                                    location=self.test_location, category=self.test_category,
                                    timestamp="test_time", caption="a test caption")

    # testing instance
    def test_instance(self):
        img = self.gallery_img
        self.assertEqual(self.gallery_img, img)

    # testing save method
    def test_save_img_method(self):
        original_len = Galleria.get_all_images()
        print(f'original len {len(original_len)}')
        self.gallery_img.save_image()
        new_len = Galleria.get_all_images()
        print(f'new len {len(new_len)}')
        self.assertTrue(len(new_len) > len(original_len))

    def test_delete_img_method(self):
        self.gallery_img.save_image()
        original_len = Galleria.objects.all()
        print(f'the categorys are{len(original_len)}')
        Galleria.delete_image(self.gallery_img.id)
        new_len = Galleria.objects.all()
        print(f'the categorys are{len(new_len)}')
        self.assertTrue((len(new_len)) == (len(original_len) - 1))

    def test_get_img_by_id_method(self):
        self.gallery_img.save_image()
        req_result = Galleria.get_image_by_id(self.gallery_img.id)
        self.assertTrue(req_result is not None)

    def test_search_gallery_method(self):
        self.gallery_img.save_image()
        search_results = Galleria.search_gallery_by_category("test category")
        print(f'The list length {len(search_results)}')
        self.assertTrue(search_results != [])

    def test_filter_gallery_list_method(self):
        self.gallery_img.save_image()
        filter_results = Galleria.filter_by_location("Kileleshwa")
        print(f'The list length {len(filter_results)}')
        self.assertTrue(filter_results != [])

