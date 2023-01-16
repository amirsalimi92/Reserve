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