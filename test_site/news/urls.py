from django.urls import path
from news.views import index, get_category, show_news, add_news, HomeView

app_name = 'news'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<slug:cat_slug>/', get_category, name='category'),
    path('news/<slug:news_slug>/', show_news, name='show_news'),
    path('addnews/', add_news, name='add_news'),

]
