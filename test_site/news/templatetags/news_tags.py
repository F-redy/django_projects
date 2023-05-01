from django import template

from news.models import Category

register = template.Library()


@register.inclusion_tag('news/tags/list_categories.html')
def show_categories(cat_selected=0):
    return {'categories': Category.objects.all(), 'cat_selected': cat_selected}
