```python
from django.contrib import admin
from django.urls import path, include
from marketplace.views import home

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('marketplace.urls')),
]

urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.BASE_DIR.parent
)