from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=199, blank=True)

    def __str__(self):
        return f'{self.name} ({self.address})'

    class Meta:
        # The line below will give the tbl the name specified in the "'
        db_table = "location"


class Category(models.Model):
    category_str = models.CharField(max_length=59)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'{self.category_str} ({self.slug})'

    class Meta:
        # The line below will give the tbl the name specified in the "'
        db_table = "category"


