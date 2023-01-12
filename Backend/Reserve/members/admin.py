from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Office, Department

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Office)
admin.site.register(Department)

# daghighe 12:45 avali