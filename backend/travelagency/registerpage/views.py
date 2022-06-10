from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm


# Create your views here.
def register_page_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginpage/')
        else:
            messages.success(request, "Try again.")
    else:
        form = RegisterForm()
    return render(request, 'tours/pages/register_page.html', {
        'form': form,
    })