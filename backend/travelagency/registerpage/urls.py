from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.register_page_view, name="register")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)