from rest_framework import serializers
from API.models import Przewoz, Karta, Car, Rate


class PrzewozSerializer(serializers.ModelSerializer):
    class Meta:
        model = Przewoz
        fields = '__all__'


class KartaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Karta
        fields = '__all__'


class CarsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class RatesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ['car_id', 'grade']
