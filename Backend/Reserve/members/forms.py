from django import forms

# my models
from .models import CustomUser

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