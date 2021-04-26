from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views import generic

from django.views.generic import TemplateView
from django.views import View

from apps.dealers.models import Country, City
from apps.dealers.forms import LoginForm, RegisterForm


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


class LoginView(View):
    form = LoginForm

    def get(self, request):
        return self._login_page(request, context={})

    def _login_page(self, request, context=None):
        context = context or {}
        context['login_form'] = self.form()

        return render(request=request, template_name='pages/login.html', context=context)

    def post(self, request):
        form = self.form(request.POST)

        if form.is_valid():
            login(request, form.cleaned_data['user'])
            return HttpResponseRedirect('/')

        return self._login_page(request, {"errors": form.non_field_errors()})


class RegisterView(View):
    form = RegisterForm

    def get(self, request):
        return self._register_page(request, context={})

    def _register_page(self, request, context=None):
        context = context or {}
        context['register_form'] = self.form()

        return render(request=request, template_name='pages/register.html', context=context)

    def post(self, request):
        form = self.form(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/')

        return self._register_page(request, {"errors": form.non_field_errors()})


@login_required(login_url='/login/')
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')
















