from django.urls import path
from news.views import add_news, HomeView, NewsByCategory, ViewNews

app_name = 'news'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<slug:cat_slug>/', NewsByCategory.as_view(), name='category'),
    path('news/<slug:news_slug>/', ViewNews.as_view(), name='show_news'),
    path('addnews/', add_news, name='add_news'),

]
