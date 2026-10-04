from django.urls import path
from . import views
from .views import home, districts
urlpatterns = [
    path('', home, name='home'),
    path('districts/', districts, name='districts'),
    path(
        'district/<int:district_id>/',
        views.district_detail,
        name='district_detail'
    ),
    path(
        'destination/<int:destination_id>/',
        views.destination_detail,
        name='destination_detail'
    ),
    path(
        'travel-routes/',
        views.travel_routes,
        name='travel_routes'
    ),
    path(
        'favorite/<int:destination_id>/',
        views.toggle_favorite,
        name='toggle_favorite'
    ),
    path(
        'favorites/',
        views.my_favorites,
        name='my_favorites'
    ),
    path(
        'signup/',
        views.signup,
        name='signup'
    ),
    path(
        'review/<int:destination_id>/',
        views.add_review,
        name='add_review'
    ),
    path(
        'hotels/',
        views.hotels,
        name='hotels'
    ),
]