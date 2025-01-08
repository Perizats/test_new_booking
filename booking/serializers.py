from rest_framework import serializers
from .models import *


class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'age', 'phone_number', 'user_role']


class CountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name',]


class HotelListSerializers(serializers.ModelSerializer):
    country = CountrySerializers(many=True, read_only=True)
    hotel_owner = ProfileItemSerializers(read_only=True)

    class Meta:
        model = Hotel
        fields = ['hotel_name', 'country', 'hotel_image', 'hotel_stars', 'city']


class HotelDetailSerializers(serializers.ModelSerializer):
    country = CountrySerializers(many=True, read_only=True)
    hotel_owner = ProfileItemSerializers(read_only=True)

    class Meta:
        model = Hotel
        fields = ['hotel_name', 'hotel_owner', 'country', 'hotel_image',  'hotel_video', 'hotel_stars',
                  'owner', 'city', 'description', 'address']


class RoomImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ['room_image', ]


class RoomListSerializers(serializers.ModelSerializer):
    room_image = RoomImageSerializers(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['room_image', ]


class RoomDetailSerializers(serializers.ModelSerializer):
    hotels_room = HotelListSerializers(many=True ,read_only=True)

    class Meta:
        model = Room
        fields = ['room_number', 'room_type', 'status',
                  'room_description', 'room_price', 'hotels_room']


class ReviewSerializers(serializers.ModelSerializer):
    user = ProfileItemSerializers(read_only=True)

    class Meta:
        model = Review
        fields = ['profile_review', 'text', 'date']


class FavoriteHotelSerializers(serializers.ModelSerializer):
    favorite = CountrySerializers(many=True, read_only=True)
    hotel = HotelListSerializers(many=True, read_only=True)
    class Meta:
        model = FavoriteHotel
        fields = ['favorite', 'hotel', 'selected']


class BookingSerializers(serializers.ModelSerializer):
    booking_user = ProfileSerializers(read_only=True)
    booking_hotel = HotelListSerializers(read_only=True)
    booking_room = RoomDetailSerializers(read_only=True)

    class Meta:
        model = Booking
        fields = ['booking_user', 'booking_hotel', 'booking_room',
                  'booking_price', 'check_in', 'check_out', 'status_book']


class HistorySerializers(serializers.ModelSerializer):
    user = ProfileSerializers(read_only=True)
    hotel = HotelListSerializers(read_only=True)
    booking = BookingSerializers(read_only=True)
    total_price = serializers.IntegerField(read_only=True)

    class Meta:
        model = History
        fields = ['user', 'hotel', 'booking', 'total_price']


class BookSerializer(serializers.ModelSerializer):
    book_hotels = HotelListSerializers(many=True ,read_only=True)
    book_country = CountrySerializers(many=True ,read_only=True)
    book_room = RoomDetailSerializers(many=True ,read_only=True)
    book_image = RoomImageSerializers(many=True ,read_only=True)

    class Meta:
        model = Book
        fields = ['book_hotels', 'book_country', 'book_room', 'book_image']