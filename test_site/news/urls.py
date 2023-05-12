from django.urls import path
from news.views import HomeView, NewsByCategory, ViewNews, CreateNews

app_name = 'news'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('page/<int:page>/', HomeView.as_view(), name='paginator'),
    path('category/<slug:cat_slug>/', NewsByCategory.as_view(), name='category'),
    path('news/<slug:news_slug>/', ViewNews.as_view(), name='show_news'),
    path('addnews/', CreateNews.as_view(), name='add_news'),

]
