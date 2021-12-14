from django.contrib import admin
from .models import Przewoz, Karta, Car, Rate
# Register your models here.

admin.site.register(Przewoz)
admin.site.register(Karta)
admin.site.register(Car)
admin.site.register(Rate)
