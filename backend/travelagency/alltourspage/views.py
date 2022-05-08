from django.shortcuts import render
from mainpage.models import TourModel, AdditionalInfoModel, DepartureInfoModel

# Create your views here.
def alltours_view(request):
    tours = TourModel.objects.all()
    context = {"tours": tours}
    return render(request, "tours/pages/alltours_page.html", context)


def showtour_view(request, id):
    tours = TourModel.objects.get(id=id)
    addinfo = AdditionalInfoModel.objects.get(id=id)
    departures = DepartureInfoModel.objects.get(id=id)
    context = {"tours": tours, "addinfo": addinfo, "departures": departures}
    return render(request, "tours/pages/tourpage.html", context)
