from django.test import TestCase
from .models import Service
from decimal import Decimal


class ServiceModelTest(TestCase):

    def test_service_creation(self):
        service = Service.objects.create(
            name="Apartment Cleaning",
            description="Test cleaning service"
        )

        self.assertEqual(service.name, "Apartment Cleaning")
        self.assertTrue(service.is_active)

    def test_booking_commission_calculation(self):
        from django.contrib.auth.models import User
        from .models import ServiceProvider, ProviderService, Booking

        service = Service.objects.create(
            name="Deep Cleaning",
            description="Test"
        )

        user = User.objects.create_user(
            username="provider_test",
            password="123456"
        )

        provider = ServiceProvider.objects.create(
            user=user,
            full_name="Test Provider",
            phone="123456789",
            city="Moscow"
        )

        provider_service = ProviderService.objects.create(
            provider=provider,
            service=service,
            price=Decimal("100.00"),
            duration_hours=2
        )

        booking = Booking.objects.create(
            customer_name="Ahmed",
            customer_phone="123456",
            provider_service=provider_service,
            booking_date="2026-06-01",
            start_time="10:00",
            end_time="12:00",
            address="Test Address",
            total_price=Decimal("100.00")
        )

        self.assertEqual(
            booking.commission_amount,
            Decimal("10.00")
        )

        self.assertEqual(
            booking.provider_earning,
            Decimal("90.00")
        )
        
    def test_services_api_returns_200(self):
        from django.urls import reverse

        Service.objects.create(
            name="Office Cleaning",
            description="Test Service"
        )

        response = self.client.get(
            reverse("api-services")
        )

        self.assertEqual(
            response.status_code,
            200
        )