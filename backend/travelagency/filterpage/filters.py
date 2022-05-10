import django_filters

from mainpage.models import *


class TicketFilter(django_filters.FilterSet):
    class Meta:
        model = TourModel
        fields = ['name', 'price', 'nightamount', 'additionalinformation__country', 'departureinformation__departureplace']
        exlude = ['image', 'id', 'description']