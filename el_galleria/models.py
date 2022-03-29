from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=199, blank=True)

    def __str__(self):
        return f'{self.name} ({self.address})'

    class Meta:
        # The line below will give the tbl the name specified in the "'
        db_table = "location"

    def save_location(self):
        return self.save()

    @classmethod
    def get_all_locations(cls):
        return cls.objects.all()

    @classmethod
    def delete_location(cls, id):
        return cls.objects.filter(id=id).delete()


class Category(models.Model):
    category_str = models.CharField(max_length=59)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'{self.category_str} ({self.slug})'

    class Meta:
        # The line below will give the tbl the name specified in the "'
        db_table = "category"

    def save_category(self):
        return self.save()

    @classmethod
    def get_all_categories(cls):
        return cls.objects.all()

    @classmethod
    def delete_category(cls, id):
        return cls.objects.filter(id=id).delete()


class Galleria(models.Model):
    img_url = models.ImageField(upload_to='galleria_imgs')
    description = models.TextField()
    timestamp = models.CharField(max_length=101)
    caption = models.CharField(max_length=88)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.caption} at ({self.location})'

    class Meta:
        # The line below will give the tbl the name specified in the "'
        db_table = "galleria"

    def save_image(self):
        return self.save()

    @classmethod
    def get_all_images(cls):
        return cls.objects.order_by("location")

    @classmethod
    def delete_image(cls, id):
        return cls.objects.filter(id=id).delete()

    @classmethod
    def get_image_by_id(cls, id):
        return cls.objects.filter(id=id).all()

    @classmethod
    def search_gallery_by_category(cls, search_str):
        search_results = cls.objects.filter(category__category_str__contains=search_str).all()
        return search_results

    @classmethod
    def filter_by_location(cls, location_str):
        filter_results = cls.objects.filter(location__name__contains=location_str).all()
        return filter_results


