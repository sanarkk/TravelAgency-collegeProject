
from django.urls import path, include


from django.conf.urls.static import static
from django.conf import settings
from .views import filterpagew_view, orderprice_view


urlpatterns = [
    path('', filterpagew_view, name='ticketfilter'),
    path('sortedbyprice/', orderprice_view, name='priceorder'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)