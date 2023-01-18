from django.contrib import admin

# my models
from Office.models import FloorsDB, Post, Reserve, bugReport

# Register your models here.
admin.site.register(FloorsDB)
admin.site.register(Post)
admin.site.register(Reserve)
admin.site.register(bugReport)