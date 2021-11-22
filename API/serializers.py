from rest_framework import serializers
from API.models import Przewoz


class PrzewozSerializer(serializers.ModelSerializer):
    class Meta:
        model = Przewoz
        fields = '__all__'
