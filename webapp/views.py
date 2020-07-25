from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from blogs.models import Post
# Create your views here.


class homeView(TemplateView):
    template_name = 'webapp/home.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        return context


class blogsView(ListView):
    model = Post
    template_name = 'webapp/blogs.html'
    ordering = ['-published_datetime']

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        return context


class profileView(TemplateView):
    template_name = 'webapp/profile.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        return context
