from django.http import HttpResponse
from django.shortcuts import render
from .models import News


def index(request):
    news = News.objects.order_by('-created_at')
    title = 'Список новостей'
    context = {
        'news_list': news,
        'title': title,
    }
    return render(request, 'news/index.html', context=context)
