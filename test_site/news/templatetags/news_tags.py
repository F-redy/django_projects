from django import template
from django.db.models import Count, F

from news.models import Category

register = template.Library()


@register.inclusion_tag('news/tags/list_categories.html')
def show_categories(cat_selected=0):
    categories = Category.objects.filter(news__is_published=True).annotate(Count('news')).filter(news__count__gt=0)
    return {'categories': categories, 'cat_selected': cat_selected}
