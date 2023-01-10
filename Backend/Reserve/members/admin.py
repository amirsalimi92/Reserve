from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Department, Office

# Register your models here.

admin.site.register(Department)
admin.site.register(Office)
admin.site.register(CustomUser)

# daghighe 12:45 avali