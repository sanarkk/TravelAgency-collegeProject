from django.shortcuts import render


# Create your views here.
def mainpage_view(request):
    return render(request, 'tours/pages/main_page.html', {})
