from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Category
from .forms import AddNewsForm

from django.views.generic import ListView, DetailView

from .utils import DataMixin


class HomeView(DataMixin, ListView):
    model = News
    title = 'Список новостей'
    cat_selected = 0

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('cat')


class NewsByCategory(ListView):
    model = News
    slug_url_kwarg = 'cat_slug'
    allow_empty = False

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
        return context


def add_news(request):
    if request.method == 'POST':
        form = AddNewsForm(request.POST)
        if form.is_valid():
            news = form.save()
            return redirect(news)
    else:
        form = AddNewsForm()
    context = {
        'title': 'Добавление новости',
        'forms': form,
    }
    return render(request, 'news/add_news.html', context=context)
