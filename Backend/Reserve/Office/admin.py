from django.contrib import admin

from Office.models import FloorsDB, Post, Reserve

# Register your models here.
admin.site.register(FloorsDB)
admin.site.register(Post)
admin.site.register(Reserve)