from django.urls import path
from .views import index, password, about

app_name = 'generator'

urlpatterns = [
    path('', index, name='index'),
    # path('passwords/', password, name='passwords'),
    path('about/', about, name='about'),
]
