from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm,
                                       UserCreationForm)
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={'class': 'form-control py-4', 'placeholder': 'Enter username'}))

    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control py-4', 'placeholder': 'Enter password'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    # first_name = forms.CharField(label='Name', widget=forms.TextInput(
    #     attrs={'class': 'form-control py-4', 'placeholder': 'Enter name'}))
    # last_name = forms.CharField(label='Surname', widget=forms.TextInput(
    #     attrs={'class': 'form-control py-4', 'placeholder': 'Enter surname'}))
    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={'class': 'form-control py-4', 'placeholder': 'Enter username'}))
    email = forms.CharField(label='email', widget=forms.EmailInput(
        attrs={'class': 'form-control py-4', 'placeholder': 'email'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control py-4', 'placeholder': 'Enter password'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(
        attrs={'class': 'form-control py-4', 'placeholder': 'Repeat password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    # def save(self, commit=True):
    #     user = super(UserRegistrationForm, self).save(commit=True)
    #     send_email_verification.delay(user.id)  # celery task
    #     return user


class UserProfileForm(UserChangeForm):
    # first_name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    # last_name = forms.CharField(label='Surname', widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    # image = forms.ImageField(label='Выберите изображение', widget=forms.FileInput(
    #     attrs={'class': 'custom-file-input'}), required=False)
    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={'class': 'form-control py-4', 'readonly': True}))
    email = forms.CharField(label='Email', widget=forms.TextInput(
        attrs={'class': 'form-control py-4', 'readonly': True}))

    class Meta:
        model = User
        fields = ('username', 'email')