from rest_framework import serializers
from .models import *


class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'age', 'phone_number', 'user_role')


class CountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('country_name',)


class HotelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('hotel_name', 'country', 'hotel_image', 'hotel_stars', 'city')


class HotelDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('hotel_name', 'country', 'hotel_image',  'hotel_video', 'hotel_stars', 'owner', 'city', 'description', 'address')


class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('room_type', )


class RoomDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('room_number', 'room_type', 'status_choices', 'room_description', 'room_price')


class RoomImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ('room_image',)


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields =('user', 'com_room', 'text', 'date')


class FavoriteHotelSerializers(serializers.ModelSerializer):
    class Meta:
        model = FavoriteHotel
        fields = ('hotel',)


class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('book_user', 'book_hotel', 'book_room', 'book_room', 'check_out', 'status_book')


class HistorySerializers(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ('hotel', 'booking_price', 'booking_date')



class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('book_hotels', 'book_country', 'book_room', 'book_image')