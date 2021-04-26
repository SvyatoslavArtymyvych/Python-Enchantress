from django.core.mail import send_mail
from rest_framework import serializers

from apps.cars.models import Order

from apps.cars.models import Car


class OrderAPISerializer(serializers.ModelSerializer):
    car = serializers.PrimaryKeyRelatedField(queryset=Car.objects)
    first_name = serializers.CharField(max_length=25)
    last_name = serializers.CharField(max_length=25)
    email = serializers.EmailField(max_length=30)
    phone = serializers.CharField(max_length=15)
    message = serializers.CharField(max_length=255)

    class Meta:
        model = Order
        fields = ['car', 'first_name', 'last_name', 'email', 'phone', 'message', ]

    def validate(self, attrs):
        car = attrs.get('car')
        email = attrs.get('email')
        first_name = attrs.get('first_name')

        order = Order.objects.filter(car=car, email=email)

        if order:
            raise serializers.ValidationError('You cannot order this car twice')

        # Email confirm msg
        # send_mail(
        #     'Order confirmed',
        #     f'Hello, {first_name}. Your order confirmed',
        #     'cardealer@test.mail',
        #     [email],
        #     fail_silently=False,
        # )

        return attrs
