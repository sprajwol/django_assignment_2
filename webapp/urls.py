from django.urls import path, include

from webapp import views as webapp_views

urlpatterns = [
    path('', webapp_views.homeView.as_view(), name='home'),
]
