from django.shortcuts import render
from mainpage.models import UserInfoModel, TourModel, AdditionalInfoModel,DepartureInfoModel
from .forms import CustomerForm, TicketForm

# Create your views here.
def userdatapage_view(request, id):
    tour = TourModel.objects.get(id=id)
    addinfo = AdditionalInfoModel.objects.get(id=id)
    departures = DepartureInfoModel.objects.get(id=id)
    form12 = CustomerForm()
    form13 = TicketForm
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'tour': tour, 'form': form12, 'addinfo': addinfo, 'departures': departures, 'form13': form13}
    return render(request, 'tours/pages/userdata_page.html', context)
