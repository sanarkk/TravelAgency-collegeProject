from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from .views import userdatapage_view

urlpatterns = [
    path('ticket/<int:id>', userdatapage_view, name="buyticket"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)