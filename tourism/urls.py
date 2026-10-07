from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.HomeView.as_view(),
        name='home'
    ),

    path(
        'districts/',
        views.DistrictListView.as_view(),
        name='districts'
    ),

    path(
        'district/<int:district_id>/',
        views.DistrictDetailView.as_view(),
        name='district_detail'
    ),

    path(
        'destination/<int:destination_id>/',
        views.DestinationDetailView.as_view(),
        name='destination_detail'
    ),

    path(
        'travel-routes/',
        views.TravelRoutesView.as_view(),
        name='travel_routes'
    ),

    path(
        'favorite/<int:destination_id>/',
        views.ToggleFavoriteView.as_view(),
        name='toggle_favorite'
    ),

    path(
        'favorites/',
        views.MyFavoritesView.as_view(),
        name='my_favorites'
    ),

    path(
        'signup/',
        views.SignupView.as_view(),
        name='signup'
    ),

    path(
        'review/<int:destination_id>/',
        views.AddReviewView.as_view(),
        name='add_review'
    ),

    path(
        'hotels/',
        views.HotelListView.as_view(),
        name='hotels'
    ),
]