from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import CharField
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField
from django.core.exceptions import ValidationError
from datetime import date


class Profile(AbstractUser):
    age = models.PositiveIntegerField(validators=[MinValueValidator(18),
                                                  MaxValueValidator(80)],
                                      null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    ROLE_CHOICES = (
        ('owner', 'owner'),
        ('customer', 'customer'),
    )
    user_role = models.CharField(max_length=32, choices=ROLE_CHOICES, default='customer')

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Country(models.Model):
    country_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.country_name


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=60)
    country = models.ManyToManyField(Country, related_name='country')
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='hotel_owner')
    description = models.TextField()
    hotel_video = models.FileField(upload_to='hotel_videos/', null=True, blank=True)
    hotel_image = models.ImageField(upload_to='hotel_image/')
    STARS_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    hotel_stars = models.PositiveIntegerField(null=True, blank=True)
    city = models.CharField(max_length=140)
    address = models.CharField(max_length=140)

    def __str__(self):
        return f'{self.hotel_name}, {self.owner}'


    def get_avg_rating(self):
        rating = self.ratings.all()
        if rating.exists():
            return round(sum(i.stars for i in rating) / rating.count(), 1)
        return 0


class Room(models.Model):
    hotels_room = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='room_numbers')
    room_number = models.PositiveIntegerField()
    TYPE_CHOICES = (
        ('люкс', 'люкс'),
        ('семейный', 'семейный'),
        ('одноместный', 'одноместный'),
        ('двухместный', 'двухместный'),
    )
    room_type = MultiSelectField(max_length=140, choices=TYPE_CHOICES)
    STATUS_CHOICES = (
        ('свободен', 'свободен'),
        ('забронирован', 'забронирован'),
        ('занят', 'занят')
    )
    status_choices = CharField(max_length=100, choices=STATUS_CHOICES)
    room_description = models.TextField()
    room_price = models.PositiveIntegerField(default=0)


class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='photos')
    room_image = models.ImageField(upload_to='images_rooms/')


class Review(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile_review')
    com_room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='com_room_review')
    text = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}, {self.com_room}'

class FavoriteHotel(models.Model):
    favorite = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='users_favorite')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='favorite_hotel')
    selected = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.favorite}, {self.hotel}'


class Booking(models.Model):
    booking_user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='booking_user')
    booking_hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='booking_hotel')
    booking_room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='booking_room')
    booking_price = models.PositiveIntegerField()
    check_in = models.DateField()
    check_out = models.DateField()
    STATUS_BOOK_CHOICES = (
        ('отменено', 'отменено'),
        ('подтверждено', 'подтверждено')
    )
    status_book = models.CharField(max_length=16, choices=STATUS_BOOK_CHOICES)


    def clean(self):
        super().clean()
        if self.check_in < date.today():
            raise ValidationError({'check_in': 'Дата заезда не может быть в прошлом'})
        if self.check_out <= self.check_in:
            raise ValidationError({'check_out': 'Дата выезда должна быть позже даты заезда'})

    def __str__(self):
        return f'{self.booking_room}, {self.booking_hotel}, {self.booking_room}'


class History(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='user_history')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_history')
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='date_history')

    def __str__(self):
        return f'{self.hotel}, {self.booking.check_in}, {self.booking.check_out}, {self.booking.booking_price}'



class Book(models.Model):
    book_hotels = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='books_hotels')
    book_country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='book_country')
    book_room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='book_room')
    book_image = models.ForeignKey(RoomImage, on_delete=models.CASCADE, related_name='books_image')
