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


class Galleria(models.Model):
    img_url = models.ImageField(upload_to='galleria_imgs')
    description = models.TextField()
    timestamp = models.CharField(max_length=101)
    caption = models.CharField(max_length=88)
    loc = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    cat = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.caption} at ({self.loc})'

    class Meta:
        # The line below will give the tbl the name specified in the "'
        db_table = "galleria"

