from django.db import models

from django.contrib.auth.models import User
# dar base user ma hame chiz ra az sefr mitavanim shoro konim ama ba oonyeki az base django estefade mikonim



# Create your models here.
class Office(models.Model):
    office = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.office}'

class Department(models.Model):
    department = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.department}'

class CustomUser(models.Model):
    # age = models.PositiveBigIntegerField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    # esme profile ke dar bala related kardim, dar view bekar mire vaghty minevisim request.user.profile

    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    isActive = models.BooleanField(default=True)
    email = models.EmailField(default="@hype.de")
    office = models.ForeignKey(Office, on_delete=models.PROTECT, blank=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, blank=True)

    # status_of_departments = (
    #     (1, 'Developers'), (2, 'IT & Product support'), (3, 'Product management'), 
    #     (4, 'Project leaders'), (5, 'QA'), (6, 'IT infrastructure'), 
    #     (7, 'Finance & Legal'), (8, 'Marketing'), (9, 'Sell & Solution consulting'), 
    #     (10, 'HR & people support'), (11, 'Innonspot'), (12, 'Viima'), (13, 'Administration')
    # )

    # department = models.IntegerField(choices=status_of_departments)

    # status_of_office = (
    #     (1, 'Bonn'), (2, 'Cologne'), (3, 'Frankfurt'), 
    #     (4, 'Other in germany'), (5, 'USA'), (6, 'France'), 
    #     (7, 'Other')
    # )

    # office = models.IntegerField(choices=status_of_office)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

