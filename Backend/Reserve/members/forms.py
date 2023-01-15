from django import forms
from .models import CustomUser
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'office', 'department',] 

        widgets = {
            'first_name': forms.TextInput(attrs={'id': 'profileFirstname'}),
            'last_name': forms.TextInput(attrs={'id': 'profileLastname'}),
            'email': forms.EmailInput(attrs={'id': 'profileEmail'}),
            'office': forms.Select(attrs={'id': 'profileOffice'}),
            'department': forms.Select(attrs={'id': 'profileDepartment'})
        }


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)

        widgets = {
            'username': forms.TextInput(attrs={'id': 'usernameReg', 'class': 'loginUsenameInputReg',}),
            # 'password1': forms.PasswordInput(attrs={'id': 'passwordReg', 'class': 'loginPasswordInputReg',}),
            # 'password2': forms.PasswordInput(attrs={'id': 'passwordReg2', 'class': 'loginPasswordInputReg2',}),
        }

        # def __init__(self, *args, **kwargs):
        #     super(RegisterUserForm, self).__init__(*args, **kwargs)
        #     self.fields['password1'].widget.attrs['class'] = 'loginPasswordInputReg'
        #     self.fields['password2'].widget.attrs['class'] = 'loginPasswordInputReg2'
