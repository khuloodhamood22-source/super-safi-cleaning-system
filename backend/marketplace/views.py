from rest_framework import generics
from datetime import datetime, timedelta
from .models import Service, ServiceProvider, ProviderService, Booking
from .serializers import (
    ServiceSerializer,
    ServiceProviderSerializer,
    ProviderServiceSerializer,
    BookingSerializer
)

from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def booking(request):
    return render(request, 'booking.html')

def success(request):
    return render(request, 'success.html')

class ServiceListAPIView(generics.ListAPIView):
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer


class ServiceProviderListAPIView(generics.ListAPIView):
    queryset = ServiceProvider.objects.filter(status='approved')
    serializer_class = ServiceProviderSerializer


class ProviderServiceListAPIView(generics.ListAPIView):
    queryset = ProviderService.objects.filter(is_active=True)
    serializer_class = ProviderServiceSerializer


class BookingListAPIView(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    from datetime import datetime, timedelta
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def guest_booking_create(request):
    service_id = request.data.get('service_id')
    customer_name = request.data.get('customer_name')
    customer_phone = request.data.get('customer_phone')
    booking_date = request.data.get('booking_date')
    booking_time = request.data.get('booking_time')
    address = request.data.get('address')

    provider_service = ProviderService.objects.filter(service_id=service_id, is_active=True).first()

    if not provider_service:
        return Response(
            {"error": "No provider available for this service"},
            status=status.HTTP_400_BAD_REQUEST
        )

    start_time = datetime.strptime(booking_time, "%H:%M").time()
    end_datetime = datetime.combine(datetime.today(), start_time) + timedelta(hours=provider_service.duration_hours)
    end_time = end_datetime.time()

    booking = Booking.objects.create(
        customer_name=customer_name,
        customer_phone=customer_phone,
        provider_service=provider_service,
        booking_date=booking_date,
        start_time=start_time,
        end_time=end_time,
        address=address,
        total_price=provider_service.price,
        status='pending'
    )

    return Response(
        {
            "message": "Booking created successfully",
            "booking_id": booking.id,
            "status": booking.status
        },
        status=status.HTTP_201_CREATED
    )