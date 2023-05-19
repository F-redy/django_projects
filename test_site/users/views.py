from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin

from common.views import DataMixin
from users.forms import UserRegistrationForm, UserLoginForm


class UserRegistrationView(DataMixin, SuccessMessageMixin, CreateView):
    model = User
    title = 'Регистрация'
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_message = '%(username) был создан!'
    error_message = 'Ошибка создания пользователя'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('news:home')

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            username=self.object.username,
        )


class UserLoginView(DataMixin, SuccessMessageMixin, LoginView):
    form_class = UserLoginForm
    title = 'Авторизация'
    template_name = 'users/login.html'
    success_url = reverse_lazy('news:home')
