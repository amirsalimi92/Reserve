from django.shortcuts import render

# work with class instead of def
from django.views.generic import ListView

# my databases
from Office.models import FloorsDB

# Create your views here.


# new version
def first_floor(request):
    datas = FloorsDB.objects.filter(floor = 1)
    context = {
        "datas": datas,
    }

    return render(request, "Office/first.html", context)

def second_floor(request):
    datas = FloorsDB.objects.filter(floor = 2)
    context = {
        "datas": datas,
    }

    return render(request, "Office/second.html", context)


# class Third_floor(ListView):
#     model = FloorsDB
#     template_name = "Office/third.html"
#     context_object_name = "datas"


def third_floor(request):
    datas = FloorsDB.objects.filter(floor = 3)
    context = {
        "datas": datas,
    }

    return render(request, "Office/third.html", context)