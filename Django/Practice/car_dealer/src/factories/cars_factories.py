import factory
from datetime import date

from src.apps.cars import models
from . import dealer_factories


class ColorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Color

    name = 'Blue'


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Brand

    name = 'BMW'


class ModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Model

    brand_id = factory.SubFactory(BrandFactory)
    name = 'X5'


class CarFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Car

    color_id = factory.SubFactory(ColorFactory)
    dealer_id = factory.SubFactory(dealer_factories.DealerFactory)
    model_id = factory.SubFactory(ModelFactory)
    engine_type = 'V Engine'
    population_type = 'u'
    price = 15999.0
    fuel_type = 'g'
    status = 'n'
    doors = 4
    capacity = 4
    gear_case = 'Manual'
    number = 'BC1234AA'
    slug = 'Blah'
    sitting_place = 4
    first_registration_date = date(2020, 10, 9)
    engine_power = 300.5


class PropertyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Property

    category = 'Decor'
    name = 'Lamp'


class CarPropertyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.CarProperty

    property_id = factory.SubFactory(PropertyFactory)
    car_id = factory.SubFactory(CarFactory)


class PictureFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Picture

    car_id = factory.SubFactory(CarFactory)
    url = 'Null'
    position = 'Front'
    metadata = 'Front Photo'


class Order(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Order

    car_id = factory.SubFactory(CarFactory)
    status = 'o'
    first_name = 'Bob'
    last_name = 'Pit'
    email = 'bob.p@gmail.com'
    phone = '380631234567'
    message = 'Message text'
