from django.http import HttpResponse


# Create your views here.
from django.utils import timezone
from django.views.generic import TemplateView

from apps.dealers.models import Dealer


def home_page(request):
    return HttpResponse('<h1>Hello</h1>')


class HomePage(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['now'] = timezone.now()
        context['user'] = self.request.user
        context['dealers'] = Dealer.objects.all().order_by('-id')

        return context


