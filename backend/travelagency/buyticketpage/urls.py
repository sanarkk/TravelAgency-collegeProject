
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from .views import ticketpage_view

urlpatterns = [
    path('', ticketpage_view)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)