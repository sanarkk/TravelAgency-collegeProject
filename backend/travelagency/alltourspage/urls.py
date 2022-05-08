from django.urls import path

from django.conf.urls.static import static
from django.conf import settings
from .views import alltours_view, showtour_view

urlpatterns = [
    path('', alltours_view, name="alltours"),
    path('tour/<int:id>', showtour_view, name="tourshow")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)