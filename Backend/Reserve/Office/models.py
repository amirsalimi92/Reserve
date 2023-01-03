from django.db import models

# Create your models here.

class Floor1DB(models.Model):
    officeName = models.CharField(max_length=35)
    equipment = models.BooleanField(default=True)
    capacity = models.IntegerField()

    def __str__(self):
        return f'First floor, number {self.officeName}'

class Floor2DB(models.Model):
    officeName = models.CharField(max_length=35)
    equipment = models.BooleanField(default=True)
    capacity = models.IntegerField()

    def __str__(self):
        return f'Second floor, number {self.officeName}'

class Floor3DB(models.Model):
    officeName = models.CharField(max_length=35)
    equipment = models.BooleanField(default=True)
    capacity = models.IntegerField()

    def __str__(self):
        return f'Third floor, number {self.officeName}'