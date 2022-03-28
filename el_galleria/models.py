from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=199, blank=True)

    def __str__(self):
        return f'{self.name} ({self.address})'

    class Meta:
        # The line below will give the tbl the name specified in the "'
        db_table = "location"

