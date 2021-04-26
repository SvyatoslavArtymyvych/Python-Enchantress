from rest_framework import serializers

from apps.cars.models import Color, Model, Car, Brand


class DealerCarAPISerializer(serializers.ModelSerializer):
    color = serializers.CharField()
    model = serializers.CharField()

    def create(self, validated_data):
        validated_data['dealer'] = self.context['request'].user #Dealer.objects.get(title=self.context['request'].user)

        validated_data['color'], created = Color.objects.get_or_create(name=validated_data['color'])

        brand, created = Brand.objects.get_or_create(name=self.context['request'].user)

        validated_data['model'], created = Model.objects.get_or_create(name=validated_data['model'],
                                                                       brand=brand)

        car = Car(**validated_data)
        car.save()

        return car

    def update(self, instance, validated_data):
        validated_data['color'], created = Color.objects.get_or_create(name=validated_data['color'])

        brand, created = Brand.objects.get_or_create(name=self.context['request'].user)

        validated_data['model'], created = Model.objects.get_or_create(name=validated_data['model'],
                                                                       brand=brand)

        instance.color = validated_data['color']
        instance.model = validated_data['model']
        instance.publish = validated_data['publish']
        instance.save()

        return instance

    class Meta:
        model = Car
        exclude = ['dealer', ]


class CarPublishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        exclude = ['publish', ]
