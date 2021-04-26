from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView, TemplateView

from apps.newsletters.forms import NewsLetterModelForm

class NewsLetterView(FormView):
    form = NewsLetterModelForm

    def get(self, request):
        return self._newsletter_page(request, context={})

    def _newsletter_page(self, request, context=None):
        context = context or {}

        return render(request=request, template_name='newsletter/newsletter.html', context=context)

    def post(self, request):
        form = self.form(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect('successful/')

        return self._newsletter_page(request, {"errors": form.non_field_errors()})


class SuccessfulView(TemplateView):
    template_name = 'newsletter/successful.html'
