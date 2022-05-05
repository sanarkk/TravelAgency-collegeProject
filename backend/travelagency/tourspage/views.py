from django.http import Http404
from django.shortcuts import render

# Create your views here.
from mainpage.models import TourModel


def tour_view(request, tour_id):
    tour = TourModel.objects.get(pk=tour_id)
    if tour is not None:
        return render(request, "tours/tour.html", {"tour": tour})
    else:
        raise Http404('Tour does not exist.')