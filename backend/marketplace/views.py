from rest_framework import generics
from datetime import datetime, timedelta
from .models import Service, ServiceProvider, ProviderService, Booking
from .serializers import (
    ServiceSerializer,
    ServiceProviderSerializer,
    ProviderServiceSerializer,
    BookingSerializer
)
from .models import ServiceProvider
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

from .models import ContactMessage


def contact(request):
    if request.method == "POST":

        ContactMessage.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            message=request.POST.get("message")
        )

        return render(request, "contact_success.html")

    return render(request, "contact.html")

def booking(request):
    return render(request, 'booking.html')

def success(request):
    return render(request, 'success.html')
from .models import ProviderApplication


def provider_application(request):

    if request.method == "POST":

        ProviderApplication.objects.create(
            full_name=request.POST.get("full_name"),
            phone=request.POST.get("phone"),
            city=request.POST.get("city"),
            description=request.POST.get("description"),
            experience_years=request.POST.get("experience_years") or 0,
            commercial_register_number=request.POST.get("commercial_register_number"),
            tax_number=request.POST.get("tax_number"),
            professional_license_number=request.POST.get("professional_license_number"),
            profile_image=request.FILES.get("profile_image"),
            license_file=request.FILES.get("license_file"),
            commercial_register_file=request.FILES.get("commercial_register_file"),
        )

        return render(request, "provider_application_success.html")

    return render(request, "provider_application.html")
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