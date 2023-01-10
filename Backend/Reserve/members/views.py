from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('office/first/')
        else:
                # messages.success(request, ("There was an error. Please try again."))
                return redirect('/')
    else:
        return render(request, "Members/login.html", {})


def logout_user(request):
    logout(request)
    return redirect('/')


def register_user(request):
    form = UserCreationForm()
    context = { 'form' : form}
    return render(request, 'Members/login.html', context)