from django.urls import path, include
from django.contrib.auth.decorators import login_required

from webapp import views as webapp_views

urlpatterns = [
    path('', webapp_views.homeView.as_view(), name='home'),
    path('blogs', webapp_views.blogsView.as_view(), name='blogs'),
    path('blogview/<int:pk>', webapp_views.detailedblogView.as_view(), name='blogview'),
    path('profile', login_required(
        webapp_views.profileView.as_view()), name='profile'),
    path('profileupdate', login_required(
        webapp_views.profileView.update_profile), name='profileupdate'),
    path('yourposts', login_required(
        webapp_views.yourpostsView.as_view()), name='yourposts'),
    path('yourpostsview/<int:pk>', login_required(
        webapp_views.yourpostdetailviewView.as_view()), name='yourpostsview'),
    path('yournewpost', login_required(
        webapp_views.yournewpostView.as_view()), name='yournewpost'),
    path('yourpostsview/<int:pk>/edit', login_required(
        webapp_views.yourpostseditView.as_view()), name='yourpostsedit'),
    path('yourpostsview/<int:pk>/delete', login_required(
        webapp_views.yourpostsdeleteView.as_view()), name='yourpostsdelete'),
]
