from django.urls import path, include
from django.contrib.auth.decorators import login_required

from webapp import views as webapp_views

urlpatterns = [
    path('', webapp_views.homeView.as_view(), name='home'),
    path('profile', login_required(
        webapp_views.profileView.as_view()), name='profile'),
]
