from django.shortcuts import render
from mainpage.models import TourModel

# Create your views here.
def alltours_view(request):
    tours = TourModel.objects.all()
    context = {'tours': tours}
    return render(request, "tours/pages/alltours_page.html", context)
