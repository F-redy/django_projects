from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Category
from .forms import AddNewsForm

from django.views.generic import ListView

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
        category = get_object_or_404(Category, slug=self.kwargs['cat_slug'])
        context['cat_selected'] = category.pk
        context['title'] = f'Новости: {category.title}'
        return context

    def get_queryset(self):
        return News.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')


def get_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    news = News.objects.filter(cat_id=category.pk)
    context = {
        'object_list': news,
        'title': f'Новости: {category.title}',
        'cat_selected': category.pk,
    }
    return render(request, 'news/news_list.html', context=context)


def show_news(request, news_slug):
    news = get_object_or_404(News, slug=news_slug)
    context = {
        'news': news,
        'title': news.title,
        'cat_selected': news.cat_id
    }
    return render(request, 'news/news.html', context=context)


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
