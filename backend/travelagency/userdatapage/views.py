from django.shortcuts import render
from mainpage.models import TourModel, AdditionalInfoModel,DepartureInfoModel, TicketModel
from .forms import TicketForm

# Create your views here.
def userdatapage_view(request, id):
    tour = TourModel.objects.get(id=id)
    addinfo = AdditionalInfoModel.objects.get(id=id)
    departures = DepartureInfoModel.objects.get(id=id)
    ticket = TicketModel.objects.get(id=id)
    form13 = TicketForm
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'tour': tour, 'addinfo': addinfo, 'departures': departures, 'form13': form13, 'ticket': ticket}
    return render(request, 'tours/pages/userdata_page.html', context)
