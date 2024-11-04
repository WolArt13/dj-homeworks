from django.db import models
from django.utils.text import slugify

class Phone(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    image = models.URLField(verbose_name="Фото")
    price = models.FloatField(max_length=28, verbose_name="Цена")
    release_date = models.DateField(verbose_name="Дата выпуска")
    lte_exists = models.BooleanField(verbose_name="Наличие LTE")
    slug = models.SlugField(verbose_name="slug_name")

    def save(self, *args, **kwargs):
        if not self.slug:  # Если slug еще не установлен
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
