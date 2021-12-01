from rest_framework import serializers
from API.models import Przewoz, Karta


class PrzewozSerializer(serializers.ModelSerializer):
    class Meta:
        model = Przewoz
        fields = '__all__'


class KartaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Karta
        fields = '__all__'