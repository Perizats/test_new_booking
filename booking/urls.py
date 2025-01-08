from rest_framework import routers
from .views import *
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'country/', CountryViewSet, basename='country_list')
router.register(r'review', ReviewViewSet, basename='review_list')
router.register(r'history', HistoryViewSet, basename='history_list')


urlpatterns = [
    path('', BookAPIView.as_view(), name='book_list'),
    path('', include(router.urls)),
    path('myhotel/', HotelListAPIView.as_view(), name='hotel_list'),
    path('myhotel<int:id>/', HotelDetailAPIView.as_view(), name='hotel_detail'),
    path('profile/', ProfileListAPIView.as_view(), name='profile_list'),
    path('profile<int:id>/', ProfileItemAPIView.as_view(), name='profile_detail'),
    path('room/', RoomListAPIView.as_view(), name='room_list'),
    path('room<int:id>/', RoomDetailAPIView.as_view(), name='room_detail'),
    path('book/', BookAPIView.as_view(), name='book_list'),
    path('room_image/', RoomListAPIView.as_view(), name='room_image_list')
]