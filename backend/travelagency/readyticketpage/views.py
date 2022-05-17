from django.shortcuts import render
from mainpage.models import TicketModel, TourModel

# Create your views here.
def readyticketpage_view(request, id):
    ticket = TicketModel.objects.get(id=id)
    tour = TourModel.objects.get(id=id)
    id = id
    context = {'ticket': ticket, 'ticket_id': id, 'tour': tour}
    return render(request, 'tours/pages/successfulbuy_page.html', context)