from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import mainpage_view

urlpatterns = [
    path('', mainpage_view, name='hottourspage')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)