from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

# work with class instead of def
from django.views.generic import ListView

# my databases
from Office.models import FloorsDB, Post
from members.models import CustomUser
from members import views as memberView

from Office.forms import PostEditForm, ReserveAddForm

# Create your views here.


# new version
def first_floor(request):

    customId = memberView.userFinder(request)

    if request.method == 'POST':
        officeAdd = ReserveAddForm(request.POST, initial={'staff': memberView.userFinder(request)})


        if officeAdd.is_valid:
            officeAdd.save()

            return redirect('/office/first')

    else:
        officeAdd = ReserveAddForm(initial={'staff': memberView.userFinder(request)})

    context = {
        "office": officeAdd,
    }

    # datas = FloorsDB.objects.filter(floor = 1)
    # context = {
    #     "datas": datas,
    #     "post": memberView.notif(request)
    # }

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


def about_page(request):
    return render(request, 'Settings/about.html', {})

def report_bugs(request):
    return render(request, "Settings/report.html", {})

def post_view(request):
    return render(request, 'Settings/post.html', {})


def post_view(request):
    post = Post.objects.all()

    if request.method == 'POST':
        postForm = PostEditForm(request.POST)
        if postForm.is_valid:
            postForm.save()

            return redirect('/settings/post/')
    
    else:
        postForm = PostEditForm()


    context = {
        "posts": post,
        "postForm": postForm,
    }

    return render(request, "Settings/post.html", context)