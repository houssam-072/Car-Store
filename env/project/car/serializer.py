from rest_framework import serializers
from .models import Car, BuyCar

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class BuyCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyCar
        fields = '__all__'