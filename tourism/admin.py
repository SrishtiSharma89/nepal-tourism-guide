from django.contrib import admin
from .models import District, Destination, Hotel, TravelRoute, Favorite, Review
# Register your models here.
admin.site.register(District)
admin.site.register(Destination)
admin.site.register(Hotel)
admin.site.register(TravelRoute)
admin.site.register(Favorite)
admin.site.register(Review)