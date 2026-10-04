from django.shortcuts import render, get_object_or_404, redirect
from .models import District, Destination, Favorite, Hotel, TravelRoute, Review
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def home(request):
    return render(request, 'tourism/home.html')


def districts(request):

    search = request.GET.get('search', '').strip()

    if search:

        # Search by district name
        districts = District.objects.filter(
            name__icontains=search
        )

        # Search by popular name
        popular_districts = District.objects.filter(
            popular_name__icontains=search
        )

        # Combine district searches
        districts = (
            districts | popular_districts
        ).distinct()

        # Search destinations by destination name
        destinations = Destination.objects.filter(
            name__icontains=search
        )

        # Search destinations by district name
        district_destinations = Destination.objects.filter(
            district__name__icontains=search
        )

        # Search destinations by district popular name
        popular_destinations = Destination.objects.filter(
            district__popular_name__icontains=search
        )

        # Combine destination searches
        destinations = (
            destinations |
            district_destinations |
            popular_destinations
        ).distinct()

    else:

        districts = District.objects.all()

        destinations = Destination.objects.none()

    return render(
        request,
        'tourism/districts.html',
        {
            'districts': districts,
            'destinations': destinations,
            'search': search
        }
    )

def district_detail(request, district_id):
    district = get_object_or_404(District, id=district_id)
    destinations = Destination.objects.filter(district=district)

    return render(
        request,
        'tourism/district_detail.html',
        {
            'district': district,
            'destinations': destinations
        }
    )


def destination_detail(request, destination_id):

    destination = get_object_or_404(
        Destination,
        id=destination_id
    )

    hotels = Hotel.objects.filter(
        destination=destination
    )

    reviews = Review.objects.filter(
        destination=destination
    ).order_by('-created_at')

    is_favorite = False

    if request.user.is_authenticated:

        is_favorite = Favorite.objects.filter(
            user=request.user,
            destination=destination
        ).exists()

    return render(
        request,
        'tourism/destination_detail.html',
        {
            'destination': destination,
            'hotels': hotels,
            'is_favorite': is_favorite,
            'reviews': reviews
        }
    )

def travel_routes(request):

    routes = TravelRoute.objects.all()

    route_data = []

    for route in routes:

        route_data.append({
            'from_location': route.from_location,
            'to_location': route.to_location,
            'from_latitude': route.from_latitude,
            'from_longitude': route.from_longitude,
            'to_latitude': route.to_latitude,
            'to_longitude': route.to_longitude,
            'transport_type': route.transport_type,
            'distance': route.distance,
        })

    from_locations = (  #this will ask django: Give me only the unique locations that appear as the starting point of a route."
        TravelRoute.objects
        .values_list('from_location', flat=True)
        .distinct()
        .order_by('from_location')
    )

    return render(
        request,
        'tourism/travel_routes.html',
        {
            'routes': routes,
            'route_data': route_data,
            'from_locations': from_locations,
        }
    )

@login_required
def toggle_favorite(request, destination_id):

    destination = get_object_or_404(
        Destination,
        id=destination_id
    )

    favorite = Favorite.objects.filter(
        user=request.user,
        destination=destination
    ).first()

    if favorite:
        favorite.delete()
    else:
        Favorite.objects.create(
            user=request.user,
            destination=destination
        )

    return redirect(
        'destination_detail',
        destination_id=destination.id
    )

@login_required
def my_favorites(request):

    favorites = Favorite.objects.filter(
        user=request.user
    ).select_related('destination')

    return render(
        request,
        'tourism/favorites.html',
        {
            'favorites': favorites
        }
    )

def signup(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:

            return render(
                request,
                'tourism/signup.html',
                {
                    'error': 'Passwords do not match.'
                }
            )

        if User.objects.filter(username=username).exists():

            return render(
                request,
                'tourism/signup.html',
                {
                    'error': 'Username already exists.'
                }
            )

        user = User.objects.create_user(
            username=username,
            password=password
        )
        return redirect('login')

    return render(
        request,
        'tourism/signup.html'
    )

@login_required
def add_review(request, destination_id):

    destination = get_object_or_404(
        Destination,
        id=destination_id
    )

    if request.method == 'POST':

        rating = request.POST.get('rating')
        comment = request.POST.get('comment').strip()

        if not rating:
            return redirect(
                'destination_detail',
                destination_id=destination.id
            )

        rating = int(rating)

        if rating < 1 or rating > 5:
            return redirect(
                'destination_detail',
                destination_id=destination.id
            )

        Review.objects.create(
            user=request.user,
            destination=destination,
            rating=rating,
            comment=comment
        )

    return redirect(
        'destination_detail',
        destination_id=destination.id
    )

def hotels(request):

    hotels = Hotel.objects.all()

    return render(
        request,
        'tourism/hotels.html',
        {
            'hotels': hotels
        }
    )

