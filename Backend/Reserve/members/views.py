from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm

# my databases
from django.contrib.auth.models import User
from .models import CustomUser
from Office.models import Post

# my forms
from .forms import ProfileEditForm


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/members/profile/')
        else:
            return redirect('/')
    else:
        return render(request, "Members/login.html", {})



def logout_user(request):
    logout(request)
    return redirect('/')



def register_profile(request):
    if request.method == 'POST':
        profileRegister = UserCreationForm(request.POST, request.FILES)
        if profileRegister.is_valid():
            user = User.objects.create_user(username= profileRegister.cleaned_data['username'],
            password = profileRegister.cleaned_data['password1'], is_staff=True)

            # we can write like above or we can write in next line:
            # user.is_staff = True

            user.save()
            profileCustom = CustomUser(user=user)
            profileCustom.save()

            # Activation link
            # for activation link, we should have the email at register
            # try:
            #     send_mail('Register successful', "Dear user,\nYour are successfully registered.\nIt's a link for you to active your account: http://127.0.0.1:8000/\nPlease edit your informations after first login.\n\nBest regards,\nReserve", 'reserve.app@hotmail.com', ['amir.salimi1810@gmail.com'],)
            # except BadHeaderError:
            #     return HttpResponse('Invalid')

            return redirect('/')

    else:
        profileRegister = UserCreationForm()

    context = {'form' : profileRegister}

    return render(request, "Members/register.html", context)



@login_required
def profileView(request):
    profile = request.user.profile

    
    context = {
        "profile": profile,
    }

    return render(request, "Members/profile.html", context)



@login_required
def profileEdit(request, profile_id):
    profile = CustomUser.objects.get(pk = profile_id)

    if request.method == 'POST':
        profileForm = ProfileEditForm(request.POST, instance=profile)
        if profileForm.is_valid:
            profileForm.save()

            # try to have some data for email
            firstName = profile.first_name
            lastName = profile.last_name
            emailUser = profile.email
            email = str(emailUser)
            if (emailUser is None):
                email = 'amir.salimi1810@gmail.com'
            text = f'Welcome {firstName} {lastName} to our community. \n\nYour profile is changed successfully. \nIf you have any question, you can just easy reply this email. \n\n\nGood Luck!\nReserve'
            

            try:
                send_mail('Reserve App', text, 'reserve.app@hotmail.com', [email],)
            except BadHeaderError:
                return HttpResponse('Invalid')


            return redirect('/members/profile/')

    else:
        profileForm = ProfileEditForm(instance=profile)

    
    context = {
        "profileForm" : profileForm,
        "profile": profile,
    }

    return render(request, "Members/editProfile.html", context)


class PasswordChangeView(PasswordChangeView):
    from_class = PasswordChangeForm
    success_url = reverse_lazy('profile')
    # inja bayad az name haye ke dar url dadim estefade konim


'''***Some function to make easy our works and give easy 
the data for working with database***'''

# You can use this def in context to know about post
def notif(request):
    # Give the data for post
    userId = request.user.id
    user = CustomUser.objects.get(user_id=userId)
    customId = user.id
    notif = 0
    post = Post.objects.all()
    for counter in post:
        if counter.staff_id == customId:
            notif += 1
  
    return notif



# Give the user data
def userFinder(request):
        userId = request.user.id
        staff = CustomUser.objects.get(user_id = userId)
        staffId = staff.id

        return staffId

def userFinderEmail(request):
    userId = request.user.id
    staff = CustomUser.objects.get(user_id = userId)
    staffEmail = staff.email

    return staffEmail

def userFinderName(request):
    userId = request.user.id
    staff = CustomUser.objects.get(user_id = userId)
    staffName = staff.first_name

    return staffName

def userFinderLastname(request):
    userId = request.user.id
    staff = CustomUser.objects.get(user_id = userId)
    staffFamily = staff.last_name

    return staffFamily