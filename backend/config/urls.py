from django.contrib import admin
from django.urls import path, include
from marketplace.views import home, about, services, contact, booking, success

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('contact/', contact, name='contact'),
    path('booking/', booking, name='booking'),
    path('success/', success, name='success'),

    path('admin/', admin.site.urls),
    path('api/', include('marketplace.urls')),
]

urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.BASE_DIR.parent
)