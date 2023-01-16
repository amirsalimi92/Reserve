from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail


# my databases
from Office.models import FloorsDB, Post
from members import views as memberView
from Office.forms import PostEditForm, ReserveAddForm

# Create your views here.


# new version
@login_required
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

    return render(request, "Office/first.html", context)

@login_required
def second_floor(request):
    datas = FloorsDB.objects.filter(floor = 2)
    context = {
        "datas": datas,
    }

    return render(request, "Office/second.html", context)

@login_required
def third_floor(request):
    datas = FloorsDB.objects.filter(floor = 3)
    context = {
        "datas": datas,
    }

    return render(request, "Office/third.html", context)


@login_required
def about_page(request):
    return render(request, 'Settings/about.html', {})

@login_required
def report_bugs(request):
    return render(request, "Settings/report.html", {})


@login_required
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

@login_required
def postDelete(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()

    return redirect('/settings/post/')