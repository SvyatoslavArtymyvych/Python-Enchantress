from rest_framework import serializers

from apps.cars.models import Color, Model, Car


class CarAPISerializer(serializers.ModelSerializer):
    color = serializers.CharField(source='color.name')
    dealer = serializers.CharField(source='dealer.title')
    brand = serializers.CharField(source='model.brand.name')
    model = serializers.CharField(source='model.name')

    class Meta:
        model = Car
        exclude = ['publish', 'views']
