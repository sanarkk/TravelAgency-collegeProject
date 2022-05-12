from django.shortcuts import render
from .filters import TicketFilter
from mainpage.models import TourModel, AdditionalInfoModel

# Create your views here.
def filterpagew_view(request):
    tours = TourModel.objects.all()
    myfilter = TicketFilter(request.GET, queryset=tours)
    tours = myfilter.qs
    context = {'filter': myfilter, 'tours':tours}
    return render(request, 'tours/pages/filterpage.html', context)


def orderprice_view(request):
    tours_sorted = TourModel.objects.all().order_by('-price')
    context = {'tours_sorted': tours_sorted}
    return render(request, 'tours/pages/orderpricepage.html', context)