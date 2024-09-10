from django.db import models
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=200, verbose_name='Назавание')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='')

    class Meta:
        ordering = ['name']

    indexes = [
        models.Index(fields=['name']),
    ]
    verbose_name = 'Тег'
    verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:painting_list_by_tag', args=(self.slug,))


class Painting(models.Model):
    tag = models.ManyToManyField(Tag, related_name='paintings', verbose_name='Теги')
    name = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='pictures/%Y/%m/%d', blank=True, verbose_name='Изображение')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    available = models.BooleanField(default=True, verbose_name='В наличии')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated = models.DateTimeField(auto_now=True, verbose_name='Изменено')

    class Meta:
        ordering = ['name']

    indexes = [
        models.Index(fields=['id', 'slug']),
        models.Index(fields=['name']),
        models.Index(fields=['-created']),
    ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:painting_detail', args=(self.pk, self.slug,))