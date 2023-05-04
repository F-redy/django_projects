from django.urls import path
from news.views import get_category, show_news, add_news, HomeView, NewsByCategory

app_name = 'news'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<slug:cat_slug>/', NewsByCategory.as_view(), name='category'),
    path('news/<slug:news_slug>/', show_news, name='show_news'),
    path('addnews/', add_news, name='add_news'),

]
