"""travelagency URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from tourspage import views
from django.conf.urls.static import static
from django.conf import settings
from loginpage.views import loginpage_view, logout_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tours/<int:tour_id>', views.tour_view),
    path('', include('django.contrib.auth.urls')),
    path('', include('loginpage.urls')),
    path('hottours/', include('mainpage.urls')),
    path('logout_user/', logout_user, name='logout_user'),
    path('alltours/', include('alltourspage.urls'), name="alltours"),
    path('buyticket/', include('userdatapage.urls'), name="buyticket"),
    path('filterticket/', include('filterpage.urls'), name="filterticket"),
    path('allticketspage/', include('allticketspage.urls'), name='alltickets'),
    path('buyedticket/', include('readyticketpage.urls'), name='readyticket'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
