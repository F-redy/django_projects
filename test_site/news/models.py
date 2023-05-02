from django.urls import reverse
from slugify import slugify
from django.db import models


class News(models.Model):
    title = models.CharField('Наименование', max_length=250)
    content = models.TextField('Контент')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата изменения', auto_now=True)
    photo = models.ImageField('фото', upload_to='photo/%Y/%m/%d/', blank=True)  # Y-год; m-месяц; d-день.
    is_published = models.BooleanField('Опубликовано', default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория', null=True)
    slug = models.SlugField('url', max_length=250, blank=True, null=True, unique=True)

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify(str(self.title))
        super(News, self).save(force_insert=False, force_update=False, using=None, update_fields=None)

    def get_absolute_url(self):
        return reverse('news:show_news', kwargs={'news_slug': self.slug})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ('-created_at',)


class Category(models.Model):
    title = models.CharField('Категория', max_length=100, db_index=True)
    slug = models.SlugField('url', max_length=100, blank=True, null=True, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news:category', kwargs={'cat_slug': self.slug})

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify(str(self.title))
        super(Category, self).save(force_insert=False, force_update=False, using=None, update_fields=None)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('title',)
