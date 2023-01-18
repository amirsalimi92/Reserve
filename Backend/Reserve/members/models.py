from django.db import models

# import user from django
from django.contrib.auth.models import User
# dar base user ma hame chiz ra az sefr mitavanim shoro konim ama ba oonyeki az base django estefade mikonim



class Office(models.Model):
    office = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.office}'


class Department(models.Model):
    department = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.department}'


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    # esme profile ke dar bala related kardim, dar view bekar mire vaghty minevisim request.user.profile

    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    isActive = models.BooleanField(default=True)
    email = models.EmailField(blank=True, null=True)
    office = models.ForeignKey(Office, on_delete=models.PROTECT, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

