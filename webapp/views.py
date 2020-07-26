from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.db import transaction
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView

from django.contrib.auth.models import User
from blogs.models import Post
from login_system.forms import UserForm, ProfileForm
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
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        return context


class detailedblogView(DetailView):
    model = Post
    template_name = 'webapp/blogview.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        return context


class profileView(TemplateView):
    template_name = 'webapp/profile.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        user_form = UserForm()
        profile_form = ProfileForm()

        context['user_form'] = user_form
        context['profile_form'] = profile_form
        return context

    @staticmethod
    @transaction.atomic
    def update_profile(request):
        if request.method == 'POST':
            user_form = UserForm(request.POST, instance=request.user)
            profile_form = ProfileForm(
                request.POST, instance=request.user.profile)
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                messages.success(request, (
                    'Your profile was successfully updated!'))
                return redirect('profile')
            else:
                messages.error(request, ('Please correct the error below.'))
        else:
            user_form = UserForm(instance=request.user)
            profile_form = ProfileForm(instance=request.user.profile)
        return render(request, 'webapp/profile_update.html', {
            'user_form': user_form,
            'profile_form': profile_form
        })


class profileupdateView(UpdateView):
    model = User
    template_name = 'webapp/profile_update.html'
    form_class = UserForm
    success_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        user_form = UserForm()
        profile_form = ProfileForm()

        context['user_form'] = user_form
        context['profile_form'] = profile_form
        return context


class yourpostsView(ListView):
    model = Post
    template_name = 'webapp/yourposts.html'
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        return context


class yournewpostView(CreateView):
    model = Post
    template_name = 'webapp/yournewpost.html'
    fields = ['title', 'title_tag', 'category',
              'main_img', 'body', 'snippet']

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        return context
