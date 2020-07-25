from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class homeView(TemplateView):
    template_name = 'webapp/home.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        return context
