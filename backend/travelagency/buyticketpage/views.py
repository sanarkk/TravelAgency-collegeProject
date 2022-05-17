from django.shortcuts import render
from .forms import CustomerForm
from mainpage.models import TicketModel


# Create your views here.
def ticketpage_view(request):
    form12 = CustomerForm()
    context = {'form12': form12}
    return render(request, "tours/pages/userdata_page.html", context)
