from django.db import models
from django.urls import reverse


class Shops(models.Model):
    objects = None
    name = models.CharField(max_length=20, db_index=True, verbose_name="Магазины")
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name


class Categories(models.Model):
    objects = None
    name = models.CharField(max_length=20, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products", kwargs={"cat_slug": self.slug})


class Products(models.Model):
    objects = None
    name = models.TextField(blank=True, db_index=True, verbose_name="Название")
    photo = models.TextField(verbose_name="Фото")
    previous_price = models.FloatField(verbose_name="Цена")
    link = models.TextField(verbose_name='Ссылка', null=True)
    cat = models.ForeignKey("Categories", on_delete=models.CASCADE, verbose_name="Категории")
    shop = models.ForeignKey("Shops", on_delete=models.CASCADE, verbose_name="Магазины")

    def __str__(self):
        return self.name
