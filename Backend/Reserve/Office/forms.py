from django import forms

# my models
from .models import Post, Reserve, bugReport
from members.models import CustomUser

# my views
from . import views




# I want to use the date filed without extra filed like time
class DateInput(forms.DateInput):
    input_type = 'date'


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['staff', 'where']

        widgets = {
            'staff': forms.Select(attrs={'id': 'postAddInputName'}),
            'where': forms.TextInput(attrs={'id': 'postAddInputWhere' , 'placeholder' : 'Where?'})
        }

class ReserveAddForm(forms.ModelForm):
    class Meta:
        model = Reserve
        fields = ['datum', 'room', 'staff']

        widgets = {
            'room': forms.Select(attrs={'id': 'ffRoomSelector'}),
            'datum': DateInput(),
            'staff': forms.Select(attrs={'style' : 'display: none'})
        }

class bugReportForm(forms.ModelForm):
    class Meta:
        model = bugReport
        fields = ['comment',]

        widgets = {
            'comment': forms.Textarea(attrs={'id': 'reportText'})
        }