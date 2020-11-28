from django.db import models


class Category(models.Model):
    """МОДЕЛЬ КАТЕГОРИЙ"""
    name = models.CharField('Название Категории', max_length=100)
    slug = models.SlugField('url', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
