from django.db import models

# other libraries
from datetime import date

from members.models import CustomUser

# Create your models here.

class FloorsDB(models.Model):

    status_of_floors = (
        (1, 'First floor'), (2, 'Second floor'), (3, 'Third floor')
    )

    floor = models.IntegerField(choices=status_of_floors)
    officeName = models.CharField(max_length=35)
    equipment = models.BooleanField(default=True)
    capacity = models.IntegerField()

    def __str__(self):
        return f'{self.floor}, number {self.officeName}'


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