from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


# my databases
from Office.models import FloorsDB, Post, bugReport, Reserve
from members import views as memberView
from Office.forms import PostEditForm, ReserveAddForm, bugReportForm
from members.models import CustomUser

# Create your views here.


# new version
@login_required
def first_floor(request):

    customId = memberView.userFinder(request)

    if request.method == 'POST':
        officeAdd = ReserveAddForm(request.POST, initial={'staff': memberView.userFinder(request)})


        if officeAdd.is_valid:
            officeAdd.save()

            # data for email
            email = memberView.userFinderEmail(request)
            first_name = memberView.userFinderName(request)
            last_name = memberView.userFinderLastname(request)
            staffId = memberView.userFinder(request)

            giveReserveRow = Reserve.objects.filter(staff_id=staffId).last()
            officeId = giveReserveRow.room_id
            officeRow = FloorsDB.objects.get(pk=officeId)
            officeNum = officeRow.officeName
            email_text = f'Dear {first_name} {last_name},\nOffice number {officeNum} has been successfully reserved for you.\n\nCheers\nReserve'
            try:
                send_mail('Reserve the office', email_text, 'reserve.app@hotmail.com', [email],)

            except:
                return BadHeaderError('Invalid')

            return redirect('/office/first')

    else:
        officeAdd = ReserveAddForm(initial={'staff': memberView.userFinder(request)})

    context = {
        "office": officeAdd,
    }

    return render(request, "Office/first.html", context)

@login_required
def second_floor(request):
    customId = memberView.userFinder(request)

    if request.method == 'POST':
        officeAdd = ReserveAddForm(request.POST, initial={'staff': memberView.userFinder(request)})


        if officeAdd.is_valid:
            officeAdd.save()

            # data for email
            email = memberView.userFinderEmail(request)
            first_name = memberView.userFinderName(request)
            last_name = memberView.userFinderLastname(request)
            staffId = memberView.userFinder(request)

            giveReserveRow = Reserve.objects.filter(staff_id=staffId).last()
            officeId = giveReserveRow.room_id
            officeRow = FloorsDB.objects.get(pk=officeId)
            officeNum = officeRow.officeName
            email_text = f'Dear {first_name} {last_name},\nOffice number {officeNum} has been successfully reserved for you.\n\nCheers\nReserve'
            try:
                send_mail('Reserve the office', email_text, 'reserve.app@hotmail.com', [email],)

            except:
                return BadHeaderError('Invalid')

            return redirect('/office/second')

    else:
        officeAdd = ReserveAddForm(initial={'staff': memberView.userFinder(request)})

    context = {
        "office": officeAdd,
    }

    return render(request, "Office/second.html", context)

@login_required
def third_floor(request):
    customId = memberView.userFinder(request)

    if request.method == 'POST':
        officeAdd = ReserveAddForm(request.POST, initial={'staff': memberView.userFinder(request)})


        if officeAdd.is_valid:
            officeAdd.save()

            # data for email
            email = memberView.userFinderEmail(request)
            first_name = memberView.userFinderName(request)
            last_name = memberView.userFinderLastname(request)
            staffId = memberView.userFinder(request)

            giveReserveRow = Reserve.objects.filter(staff_id=staffId).last()
            officeId = giveReserveRow.room_id
            officeRow = FloorsDB.objects.get(pk=officeId)
            officeNum = officeRow.officeName
            email_text = f'Dear {first_name} {last_name},\nOffice number {officeNum} has been successfully reserved for you.\n\nCheers\nReserve'
            try:
                send_mail('Reserve the office', email_text, 'reserve.app@hotmail.com', [email],)

            except:
                return BadHeaderError('Invalid')

            return redirect('/office/third')

    else:
        officeAdd = ReserveAddForm(initial={'staff': memberView.userFinder(request)})

    context = {
        "office": officeAdd,
    }

    return render(request, "Office/third.html", context)


@login_required
def about_page(request):
    return render(request, 'Settings/about.html', {})


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


@login_required
def bugReportView(request):
    bug = bugReport.objects.all()

    if request.method == 'POST':
        bugForm = bugReportForm(request.POST)
        if bugForm.is_valid:
            bugForm.save()

            # get the last row
            findLast = bugReport.objects.all().last()
            report = findLast.comment
            

            try:
                send_mail('Report a new BUG!', report, 'reserve.app@hotmail.com', ['amir.salimi1810@gmail.com'],)
            except:
                return BadHeaderError('Invalid')

            return redirect('/settings/report/')

    else:
        bugForm = bugReportForm()

    context= {
        'bug': bug,
        'bugForm': bugForm
    }

    return render(request, "Settings/report.html", context)


@login_required
def reservedViews(request):
    offices = Reserve.objects.all()

    context = {
        'offices': offices
    }

    return render(request, 'Office/reserved.html', context)


@login_required
def reserveDelete(request, reserve_id):
    office = Reserve.objects.get(id= reserve_id)
    

    fnameWhoDeleted = memberView.userFinderName(request)
    lnameWhoDeleted = memberView.userFinderLastname(request)

    
    officeNumberId = office.room_id
    officeRow = FloorsDB.objects.get(pk=officeNumberId)
    officeName = officeRow.officeName

    staffId = office.staff_id
    whoseDeleted = CustomUser.objects.get(id = staffId)
    fnameWhoseDeleted = whoseDeleted.first_name
    lnameWhoseDeleted = whoseDeleted.last_name
    whoseDeletedEmail = whoseDeleted.email

    office.delete()

    emailText = f'Dear {fnameWhoseDeleted} {lnameWhoseDeleted}\nYour reserved office with number {officeName} is deleted by {fnameWhoDeleted} {lnameWhoDeleted}.\nIf you need still your office, then try to reserve it again.\n\nGood Luck\nReserve'

    try:
        send_mail('Your reserve is deleted', emailText, 'reserve.app@hotmail.com', [whoseDeletedEmail],)
    except:
        return BadHeaderError('Invalid')

    return redirect('/reserved/')