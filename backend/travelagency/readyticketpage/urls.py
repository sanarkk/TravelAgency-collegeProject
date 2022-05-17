from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from .views import readyticketpage_view

urlpatterns = [
    path('<int:id>', readyticketpage_view, name='readyticket12')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)