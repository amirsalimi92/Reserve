from django.contrib import admin

# my models
from .models import CustomUser, Office, Department

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Office)
admin.site.register(Department)
