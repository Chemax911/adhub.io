from django.db import models


class Category(models.Model):
    """МОДЕЛЬ КАТЕГОРИЙ"""

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField('Название Категории', max_length=100)
    slug = models.SlugField('url', max_length=100)

    def __str__(self):
        return self.name


class Condition(models.Model):
    """МОДЕЛЬ СОСТОЯНИЯ"""

    class Meta:
        ordering = ['name']
        verbose_name = 'Состояние'
        verbose_name_plural = 'Состояния'

    name = models.CharField('Пазвание', max_length=100)
    description = models.TextField('Краткое описание')

    def __str__(self):
        return self.name
