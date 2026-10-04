from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class District(models.Model):
    name = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    popular_name = models.CharField(
        max_length=100,
        blank=True
    )
    description = models.TextField()
    
    def __str__(self):
        return self.name

class Destination(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    best_time = models.CharField(max_length=100)
    image = models.ImageField(upload_to='destinations/', blank=True, null=True)

    def __str__(self):
        return self.name

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    destination = models.ForeignKey(
        Destination,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    address = models.CharField(max_length=200)
    description = models.TextField()
    price_range = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    latitude = models.FloatField()
    longitude = models.FloatField()
    image = models.ImageField(upload_to='hotels/', blank=True, null=True)

    def __str__(self):
        return self.name

class TravelRoute(models.Model):
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    transport_type = models.CharField(max_length=100)
    distance = models.CharField(max_length=50)
    estimated_time = models.CharField(max_length=50)
    description = models.TextField()
    from_latitude = models.FloatField(null=True, blank=True)
    from_longitude = models.FloatField(null=True, blank=True)
    to_latitude = models.FloatField(null=True, blank=True)
    to_longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.from_location} → {self.to_location}"

class Favorite(models.Model):

    user = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )

    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.destination.name}"

class Review(models.Model):

    user = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )

    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE
    )

    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )

    comment = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.destination.name}"