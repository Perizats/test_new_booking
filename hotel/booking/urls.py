from rest_framework import routers
from .views import *
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'country/', CountryViewSet, basename='country_list'),
router.register(r'room_image/', CountryViewSet, basename='room_list'),
router.register(r'review', ReviewViewSet, basename='review_list'),
router.register(r'history', HistoryViewSet, basename='history_list')


urlpatterns = [
    path('hotel/', include(router.urls)),
    path('', HotelAPIView.as_view(), name='hotel_list'),
    path('hotel<int>/', HotelDetailAPIView.as_view(), name='hotel_detail'),
    path('profile/', ProfileAPIView.as_view(), name='profile_list'),
    path('profile<int>/', ProfileItemAPIView.as_view(), name='profile_detail'),
    path('room/', RoomAPIView.as_view(), name='room_list'),
    path('room<int>/', RoomDetailAPIView.as_view(), name='room_detail'),
    path('book/', BookAPIView.as_view(), name='book_list')
]