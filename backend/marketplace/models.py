from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ServiceProvider(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='providers/', blank=True, null=True)
    description = models.TextField(blank=True)
    experience_years = models.PositiveIntegerField(default=0)
    response_time = models.CharField(max_length=100, blank=True)

    is_verified = models.BooleanField(default=False)
    commercial_register_number = models.CharField(max_length=100, blank=True)
    tax_number = models.CharField(max_length=100, blank=True)
    professional_license_number = models.CharField(max_length=100, blank=True)
    license_file = models.FileField(upload_to='provider_licenses/', blank=True, null=True)
    commercial_register_file = models.FileField(upload_to='commercial_registers/', blank=True, null=True)


    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return self.full_name


class ProviderService(models.Model):
    provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_hours = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.provider.full_name} - {self.service.name}"


class ProviderAvailability(models.Model):
    DAYS_OF_WEEK = (
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
    )

    provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=20, choices=DAYS_OF_WEEK)
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.provider.full_name} - {self.day_of_week} {self.start_time}-{self.end_time}"


class Booking(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )

    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=20)

    provider_service = models.ForeignKey(ProviderService, on_delete=models.CASCADE)

    booking_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    address = models.TextField()
    notes = models.TextField(blank=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    commission_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    provider_earning = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        commission_rate = Decimal('0.10')
        self.commission_amount = self.total_price * commission_rate
        self.provider_earning = self.total_price - self.commission_amount
        super().save(*args, **kwargs)

    def __str__(self):
        if self.customer:
            return f"Booking #{self.id} - {self.customer.username}"
        return f"Booking #{self.id} - {self.customer_name}"


class Review(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)

    rating = models.PositiveIntegerField()
    comment = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.provider.full_name} - {self.rating}/5"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=150)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject