from .models import News, Category
from .forms import AddNewsForm

from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .utils import DataMixin


class HomeView(DataMixin, ListView):
    model = News
    title = 'Список новостей'
    cat_selected = 0

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('cat')


class NewsByCategory(DataMixin, ListView):
    model = News
    slug_url_kwarg = 'cat_slug'
    allow_empty = False  # Если коллекция пустая будет выбрасывать ошибку 404

    def get_context_data(self, **kwargs):
        context = super(NewsByCategory, self).get_context_data(**kwargs)
        category = Category.objects.get(slug=self.kwargs['cat_slug'])
        context['cat_selected'] = category.pk
        context['title'] = f'Новости: {category.title}'
        return context

    def get_queryset(self):
        return News.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')


class ViewNews(DetailView):
    model = News
    slug_url_kwarg = 'news_slug'  # по умолчанию в url django ищет id или slug
    context_object_name = 'news'  # по умолчанию object

    def get_context_data(self, **kwargs):
        context = super(ViewNews, self).get_context_data(**kwargs)
        news = News.objects.get(slug=self.kwargs['news_slug'])
        context['title'] = news.title
        context['cat_selected'] = news.cat_id
        news.add_views()
        return context


class CreateNews(LoginRequiredMixin, CreateView):
    raise_exception = True
    form_class = AddNewsForm
    template_name = 'news/add_news.html'
