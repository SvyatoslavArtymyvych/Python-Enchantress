from django.db.models import F
from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
from django.views import View

from apps.cars.models import Car, Picture
from django.views.generic import TemplateView

from apps.cars.forms import OrderForm


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

        context['car'] = Car.objects.get(id=context['car_id'])
        Car.objects.filter(id=context['car_id']).update(views=F('views') + 1)

        return context


class OrderView(View):
    form = OrderForm

    def get(self, request, **kwargs):
        return self._order_page(request, **kwargs)

    def _order_page(self, request, context=None, **kwargs):
        context = context or {}
        context['order_form'] = self.form()

        context['car'] = Car.objects.filter(id=kwargs.get('car_id'))[0]

        return render(request=request, template_name='pages/order.html', context=context)

    def post(self, request, **kwargs):
        form = self.form(request.POST, car=kwargs.get('car_id'))

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/cars')

        return self._order_page(request, {"errors": form.non_field_errors()}, car_id=kwargs.get('car_id'))
