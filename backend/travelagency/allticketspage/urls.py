from django.urls import path

from django.conf.urls.static import static
from django.conf import settings
from .views import alltickets_view

urlpatterns = [
    path('', alltickets_view, name="allticketspage"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
