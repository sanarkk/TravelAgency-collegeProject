from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def loginpage_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('tours/1')
            # NEED TO REDIRECT ON MAINPAGE
        else:
            return render(request, 'tours/pages/login_page.html')
    else:
        return render(request, 'tours/pages/login_page.html')