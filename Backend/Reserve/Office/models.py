from django.db import models

# other libraries
from datetime import date

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



