from rest_framework import serializers

from apps.cars.models import Color, Model, Car
from apps.dealers.models import Dealer

from apps.cars.choises import POPULATIONS_TYPES_CHOICES, FUEL_TYPE_CHOICES, STATUS_CHOICES, STATUS_NEW


class CarAPISerializer(serializers.ModelSerializer):
    color = serializers.CharField(source='color.name')
    dealer = serializers.CharField(source='dealer.title')
    brand = serializers.CharField(source='model.brand.name')
    model = serializers.CharField(source='model.name')
    # engine_type = serializers.CharField(max_length=20)
    # population_type = serializers.ChoiceField(choices=POPULATIONS_TYPES_CHOICES)
    # price = serializers.FloatField()
    # fuel_type = serializers.ChoiceField(choices=FUEL_TYPE_CHOICES)
    # status = serializers.ChoiceField(choices=STATUS_CHOICES, default=STATUS_NEW)
    # doors = serializers.IntegerField()
    # capacity = serializers.FloatField()
    # gear_case = serializers.CharField(max_length=25)
    # number = serializers.CharField(max_length=15)
    # slug = serializers.CharField(max_length=20)
    # sitting_place = serializers.IntegerField(default=2)
    # first_registration_date = serializers.DateTimeField()
    # engine_power = serializers.FloatField()

    class Meta:
        model = Car
        # fields = '__all__'
        exclude = ['publish', ]
