from django.shortcuts import render


# Create your views here.
def ticketpage_view(request):
    return render(request, "tours/pages/ticket_buy.html", {})
