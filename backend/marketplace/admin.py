from django.contrib import admin
from .models import ProviderApplication
from .models import (
    Service,
    ServiceProvider,
    ProviderService,
    ProviderAvailability,
    Booking,
    Review,
    ContactMessage
)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_active']
    search_fields = ['name']


@admin.register(ServiceProvider)
class ServiceProviderAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'city', 'phone', 'is_verified', 'status']
    list_filter = ['is_verified', 'status', 'city']
    search_fields = ['full_name', 'phone', 'city']


@admin.register(ProviderService)
class ProviderServiceAdmin(admin.ModelAdmin):
    list_display = ['provider', 'service', 'price', 'duration_hours', 'is_active']
    list_filter = ['service', 'is_active']


@admin.register(ProviderAvailability)
class ProviderAvailabilityAdmin(admin.ModelAdmin):
    list_display = ['provider', 'day_of_week', 'start_time', 'end_time', 'is_available']
    list_filter = ['day_of_week', 'is_available']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'customer_name',
        'customer_phone',
        'provider_service',
        'booking_date',
        'status',
        'total_price'
    ]
    list_filter = ['status', 'booking_date']
    search_fields = ['customer_name', 'customer_phone']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['provider', 'customer', 'rating', 'created_at']
    list_filter = ['rating']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at']
    search_fields = ['name', 'email']

@admin.register(ProviderApplication)
class ProviderApplicationAdmin(admin.ModelAdmin):
    list_display = [
        'full_name',
        'phone',
        'city',
        'experience_years',
        'created_at'
    ]

    search_fields = [
        'full_name',
        'phone',
        'city'
    ]