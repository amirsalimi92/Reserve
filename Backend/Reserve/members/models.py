from django.db import models

from django.contrib.auth.models import AbstractUser, AbstractBaseUser
# dar base user ma hame chiz ra az sefr mitavanim shoro konim ama ba oonyeki az base django estefade mikonim



# Create your models here.

class Office(models.Model):
    status_of_office = (
        (1, 'Bonn'), (2, 'Cologne'), (3, 'Frankfurt'), 
        (4, 'Other in germany'), (5, 'USA'), (6, 'France'), 
        (7, 'Other')
    )

    office = models.IntegerField(choices=status_of_office)

    def __str__(self):
        return f'{self.office}'

class Department(models.Model):
    status_of_departments = (
        (1, 'Developers'), (2, 'IT & Product support'), (3, 'Product management'), 
        (4, 'Project leaders'), (5, 'QA'), (6, 'IT infrastructure'), 
        (7, 'Finance & Legal'), (8, 'Marketing'), (9, 'Sell & Solution consulting'), 
        (10, 'HR & people support'), (11, 'Innonspot'), (12, 'Viima'), (13, 'Administration')
    )

    department = models.IntegerField(choices=status_of_departments)

    def __str__(self):
        return f'{self.department}'

class CustomUser(AbstractUser):
    # age = models.PositiveBigIntegerField(null=True, blank=True)
    department = models.ForeignKey(to='Department', on_delete=models.PROTECT)
    office = models.ForeignKey(to="Office", on_delete=models.PROTECT)