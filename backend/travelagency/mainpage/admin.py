from django.contrib import admin
from .models import (
    DepartureInfoModel,
    AdditionalInfoModel,
    TourModel,
    TicketModel,
)

# Register your models here.
admin.site.register(DepartureInfoModel)
admin.site.register(AdditionalInfoModel)
admin.site.register(TourModel)
admin.site.register(TicketModel)