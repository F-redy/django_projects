from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from common.views import TitleMixin
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm


class UserLoginView(TitleMixin, LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
    title = 'Authorization'
    success_url = reverse_lazy('generator:index')


class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    title = 'Registration'
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Congratulations! You have successfully registered!'


class UserProfileView(TitleMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    title = 'Profile'
    template_name = 'users/profile.html'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))
