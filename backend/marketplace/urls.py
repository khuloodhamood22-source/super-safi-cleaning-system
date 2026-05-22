from .views import (
    ServiceListAPIView,
    ServiceProviderListAPIView,
    ProviderServiceListAPIView,
    BookingListAPIView,
    guest_booking_create
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path

urlpatterns = [
    path('services/', ServiceListAPIView.as_view(), name='api-services'),
    path('providers/', ServiceProviderListAPIView.as_view(), name='api-providers'),
    path('provider-services/', ProviderServiceListAPIView.as_view(), name='api-provider-services'),
    path('bookings/', BookingListAPIView.as_view(), name='api-bookings'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('guest-booking/', guest_booking_create, name='guest-booking'),
]