from login_system.forms import RegisterForm
from django.urls import reverse_lazy
from django.views.generic import View
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

UserModel = get_user_model()


# Create your views here.


class registerView(View):
    @staticmethod
    def register(request):
        if request.method == 'GET':
            form = RegisterForm()
            return render(request, 'login_system/register.html', {'form': form})
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            # print(form.errors.as_data())
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                mail_subject = 'Activate your account.'
                message = render_to_string('login_system/acc_active_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user),
                })
                to_email = form.cleaned_data.get('email')
                email = EmailMessage(
                    mail_subject, message, to=[to_email]
                )
                email.send()
                res = "<p>Please confirm your email address to complete the registration.</p><div class=\"login-link\"><a href=\"{% url 'login' %}\">Sign Back In</a></div><div class=\"visit-site-link\"><a href=\"{% url 'home' %}\">Visit Website</a></div>"
                return HttpResponse(res)
        else:
            form = RegisterForm()
        return render(request, 'login_system/register.html', {'form': form})

    @staticmethod
    def activate(request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = UserModel._default_manager.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        else:
            return HttpResponse('Activation link is invalid!')
