from django.db import models


# Create your models here.

class Przewoz(models.Model):
    carrier = models.CharField(max_length=100)
    plate_number = models.CharField(max_length=15)
    client = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    wage_without_car = models.IntegerField(default=0)
    date = models.DateTimeField('Pub date')

    def __str__(self):
        return self.plate_number

class Karta(models.Model):
    id_card = models.CharField(max_length=100)

