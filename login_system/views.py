from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from login_system.forms import RegisterForm
# Create your views here.


class registerView(CreateView):
    form_class = RegisterForm
    template_name = 'login_system/register.html'
    success_url = reverse_lazy('login')
