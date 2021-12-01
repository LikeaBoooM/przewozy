from django.db import models


# Create your models here.

class Przewoz(models.Model):
    carrier = models.CharField(max_length=100)
    plate_number = models.CharField(max_length=15)
    client = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    wage_without_car = models.IntegerField(default=0)
    date = models.DateField('Pub date', null=True)

    def __str__(self):
        return self.plate_number

class Karta(models.Model):
    id_card = models.CharField(max_length=100)
    registration = models.CharField(max_length=100)
    carrier = models.CharField(max_length=100)
    recipent = models.CharField(max_length=100)
    tare = models.IntegerField(default=0)
    product = models.CharField(max_length=100)
    fuel = models.IntegerField(default=0)

    def __str__(self):
        return self.id_card