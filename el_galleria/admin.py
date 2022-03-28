from django.contrib import admin

from .models import Category, Location, Galleria
# Register your models here.


# This class determines how the admin dashboard will look
class GalleriaAdmin(admin.ModelAdmin):
    # The line below will allow us to display the meetup obj items in a list with the specified columns
    # the columnnames in the models are what we've used in the strs
    list_display = ('caption', 'loc', 'timestamp')
    # The line below will allow us to have filter opts for our list of entries that appear in the admin dash
    list_filter = ('timestamp', "loc", "category")
    # The line below will pre-populate the slug field based on the title we enter,
    #  the key is the param that we'd like to pre-populate and the tuple has the entries that'll be concat'ed to create the key
    # prepopulated_fields = {'slug': ('title',)}


# This class determines how the admin dashboard will look
class LocationAdmin(admin.ModelAdmin):
    # The line below will allow us to display the meetup obj items in a list with the specified columns
    # the columnnames in the models are what we've used in the strs
    list_display = ('name', 'address')
    # The line below will allow us to have filter opts for our list of entries that appear in the admin dash
    list_filter = ('name', )
    # The line below will pre-populate the slug field based on the title we enter,
    #  the key is the param that we'd like to pre-populate and the tuple has the entries that'll be concat'ed to create the key
    # prepopulated_fields = {'slug': ('title',)}


# This class determines how the admin dashboard will look
class CategoryAdmin(admin.ModelAdmin):
    # The line below will allow us to display the meetup obj items in a list with the specified columns
    # the columnnames in the models are what we've used in the strs
    list_display = ('category_str', 'slug')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Galleria, GalleriaAdmin)

