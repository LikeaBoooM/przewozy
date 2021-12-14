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
        return self.registration


class Car(models.Model):
    make = models.CharField(max_length=180)
    model = models.CharField(max_length=180, unique=True)

    def __str__(self):
        return self.make


class Rate(models.Model):
    class Ratings(models.IntegerChoices):
        One = 1
        Two = 2
        Three = 3
        Four = 4
        Five = 5

    grade = models.IntegerField(choices=Ratings.choices)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return self.car_id.model
