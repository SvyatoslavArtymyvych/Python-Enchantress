from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views import generic

from apps.dealers.models import Country, City
from django.views.generic import TemplateView


class CountryCreateForm(generic.CreateView):
    model = Country
    fields = ['name', 'code']
    template_name = 'dealers/country_create.html'


class CountriesList(TemplateView):
    template_name = 'pages/countries.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['cities'] = City.objects.all()

        return context


# class LoginView(View):
#     def get(self, request):
#         return render(request=request,
#                       template_name='',
#                       context={})
#
#     def post(self, request):
#         user_name = request.POST.get('username')
#         password = request.POST.get('password')
#
#         if user_name and password:
#             user = authenticate(user_name=user_name, password=password)
#
#             if user:
#                 login(request, user)
#                 return HttpResponseRedirect('')
#
#         return HttpResponseRedirect('')