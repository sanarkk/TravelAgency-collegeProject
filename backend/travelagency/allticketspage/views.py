from django.shortcuts import render
from mainpage.models import TicketModel, TourModel


# Create your views here.
def alltickets_view(request):
    tickets = TicketModel.objects.all()
    context = {'tickets': tickets}
    return render(request, 'tours/pages/allticketspage.html', context)