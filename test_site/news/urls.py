from django.urls import path
from news.views import index

app_name = 'news'

urlpatterns = [
    path('', index, name='index'),
]
