from django import forms
from django.core.exceptions import ValidationError

from apps.cars.models import Order
from apps.cars.models import Car


class CarCreateForm(forms.ModelForm):
    color = forms.CharField(max_length=20, label='Color')
    model = forms.CharField(max_length=35, label='Model')
    brand = forms.CharField(max_length=35, label='Brand')
    engine_type = forms.CharField(max_length=20, label='Engine type')
    population_type = forms.CharField(max_length=1, label='Population type')
    price = forms.FloatField(label='Price')
    fuel_type = forms.CharField(max_length=1, label='Fuel type')
    status = forms.CharField(max_length=1, label='Status')
    doors = forms.IntegerField(label='Doors')
    capacity = forms.FloatField(label='Capacity')
    gear_case = forms.CharField(max_length=25, label='Gear case')
    number = forms.CharField(max_length=15, label='Number')
    slug = forms.CharField(max_length=20, label='Slug')
    sitting_place = forms.IntegerField(label='Sitting place')
    first_registration_date = forms.DateTimeField(label='First registration date')
    engine_power = forms.FloatField(label='Engine power')


class OrderForm(forms.ModelForm):
    car = forms.IntegerField(label='Car', required=False)
    first_name = forms.CharField(max_length=25, label='First Name')
    last_name = forms.CharField(max_length=25, label='Last Name')
    email = forms.CharField(widget=forms.EmailInput, max_length=30, label='Email')
    phone = forms.CharField(widget=forms.NumberInput, max_length=30, label='Phone')
    message = forms.CharField(widget=forms.Textarea, max_length=255, label='Message')

    def __init__(self, *args, car=None, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self._car = car
        # self.initial['car'] = car

    def clean_car(self):
        try:
            car = Car.objects.get(id=self._car)
        except Car.DoesNotExist:
            raise ValidationError('Car does not exist')

        return car

    class Meta:
        model = Order
        fields = ("car", "first_name", 'last_name', 'email', 'phone', 'message')

    def save(self, commit=True):
        order = super(OrderForm, self).save(commit=False)

        if commit:
            order.save()
        return order
