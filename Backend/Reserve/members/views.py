from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect


from .models import CustomUser

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


def profileView(request):
    profile = request.user.profile

    context = {
        "profile": profile,
    }

    return render(request, "Members/profile.html", context)