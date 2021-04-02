import factory

from src.apps.dealers import models


class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Country

    name = 'Ukraine'
    code = 164


class CityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.City

    name = 'Lviv'
    country_id = factory.SubFactory(CountryFactory)


class DealerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Dealer

    title = 'BMW-Dealer'
    email = 'dealer.bmw@mail.com'
    city_id = factory.SubFactory(CityFactory)
