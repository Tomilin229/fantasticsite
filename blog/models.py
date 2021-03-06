from django.db import models


class Category(models.Model):
    """Модель категорий"""
    name = models.CharField(verbose_name="Имя", max_length=100)
    slog = models.SlugField(verbose_name="url",max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"