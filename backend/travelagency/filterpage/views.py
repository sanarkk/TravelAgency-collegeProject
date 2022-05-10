from django.shortcuts import render
from .filters import TicketFilter
from mainpage.models import TourModel

# Create your views here.
def filterpagew_view(request):
    tours = TourModel.objects.all()
    myfilter = TicketFilter(request.GET, queryset=tours)
    tours = myfilter.qs
    context = {'filter': myfilter, 'tours':tours}
    return render(request, 'tours/pages/filterpage.html', context)