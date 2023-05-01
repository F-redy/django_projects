from django.http import HttpResponse
from django.shortcuts import render
from .models import News, Category


def index(request):
    news = News.objects.all()
    title = 'Список новостей'
    context = {
        'news_list': news,
        'title': title,
        'cat_selected': 0,
    }
    return render(request, 'news/index.html', context=context)


def get_category(request, cat_slug):
    category = Category.objects.get(slug=cat_slug)
    news = News.objects.filter(cat_id=category.pk)
    context = {
        'news_list': news,
        'title': category,
        'cat_selected': category.pk,
    }
    return render(request, 'news/index.html', context=context)
