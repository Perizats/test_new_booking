from rest_framework import viewsets, generics
from .serializers import *
from .models import *
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from .permissions import CheckOwner, CheckRole, ReadOnlyPermission


class ProfileListAPIView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Profile.objects.filter(id=self.request.user.id)


class ProfileItemAPIView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileItemSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
         return Profile.objects.filter(id=self.request.user.id)


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializers


class HotelListAPIView(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelListSerializers
    permission_classes = [permissions.IsAuthenticated, CheckOwner]


class HotelDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelDetailSerializers


class RoomListAPIView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomListSerializers


class RoomDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RoomImageAPIView(generics.RetrieveUpdateAPIView):
    queryset = RoomImage.objects.all()
    serializer_class = RoomImageSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
    permission_classes = [permissions.IsAuthenticated, CheckRole]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FavoriteHotelViewSet(viewsets.ModelViewSet):
    queryset = FavoriteHotel.objects.all()
    serializer_class = FavoriteHotelSerializers


class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializers


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers
    permission_classes = [permissions.IsAuthenticated, CheckRole, CheckOwner]

    def perform_create(self, serializer):
        serializer.save(booking_user=self.request.user)


class BookAPIView(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelDetailSerializers
    filter_backends = [DjangoFilterBackend ,SearchFilter, OrderingFilter]
    filterset_fields = ['country', 'city', 'price']
    search_fields = ['hotel_name',]
    ordering_fields = ['price',]
    permission_classes = [ReadOnlyPermission]