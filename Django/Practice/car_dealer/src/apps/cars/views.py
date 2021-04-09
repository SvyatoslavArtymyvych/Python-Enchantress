from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import generic

from apps.cars.models import Car, Picture
from django.views.generic import TemplateView


class ShowCars(TemplateView):
    template_name = 'pages/cars.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['cars'] = Car.objects.all()

        return context


class CarDetails(TemplateView):
    template_name = 'pages/car.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['car'] = Car.objects.filter(id=context['car_id'])[0]

        return context


class CreateCarCreatingView(generic.CreateView):
    pass
    # model = Car
    #
    # fields = ['color_id']
    #
    # template_name = 'cars/create_car_form.html'


def car_api(request, id):
    car = Car.objects.filter(id=id).first()
    if car:
        data = serializers.serialize('json', [car])
    else:
        data = '{"error":"car does not exists"}'
    return HttpResponse(data)
