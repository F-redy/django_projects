from django.urls import path
from .views import index, password

app_name = 'generator'

urlpatterns = [
    path('', index, name='index'),
    path('passwords/', password, name='passwords'),
]
