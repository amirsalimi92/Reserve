from django.db import models

#give the time
from datetime import date

# my models
from members.models import CustomUser

class FloorsDB(models.Model):

    status_of_floors = (
        (1, 'First floor'), (2, 'Second floor'), (3, 'Third floor')
    )

    floor = models.IntegerField(choices=status_of_floors)
    officeName = models.CharField(max_length=35)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return f'Number {self.officeName}'


class Post(models.Model):
    staff = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    where = models.TextField()

    def __str__(self):
        return f'{self.staff}'


class Reserve(models.Model):
     staff = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
     datum = models.DateField()
     room = models.ForeignKey(FloorsDB, on_delete=models.PROTECT)

     def __str__(self):
        return f'Office {self.room} for {self.staff} in {self.datum}'


class bugReport(models.Model):

    comment = models.TextField()

    def __str__(self):
        return f'{self.comment}'