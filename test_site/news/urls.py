from django.urls import path
from news.views import index, get_category

app_name = 'news'

urlpatterns = [
    path('', index, name='index'),
    path('category/<slug:cat_slug>/', get_category, name='category'),
]
