from django.contrib import admin
from django.utils.safestring import mark_safe

from news.models import News, Category


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'cat', 'created_at', 'updated_at', 'is_published')
    fields = ('title', 'cat', 'content', 'photo', 'get_photo', 'is_published', 'views', 'created_at', 'updated_at')
    readonly_fields = ('get_photo', 'views', 'created_at', 'updated_at')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_editable = ('is_published', 'cat')
    list_filter = ('cat',)
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width=75>')
        else:
            return '-'

    get_photo.short_description = 'Миниатюра'


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.site_title = 'Управление новостями'
admin.site.site_header = 'Управление новостями'
