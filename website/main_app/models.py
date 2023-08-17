from django.db import models


class Shops(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name="Магазины")


class Categories(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name="URL")


class Products(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name="Категория")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    shop_name = models.CharField(max_length=20, db_index=True, verbose_name="Название магазина")
    previous_price = models.FloatField(verbose_name="Цена")
    cat = models.ForeignKey("Categories", on_delete=models.PROTECT, verbose_name="Категории")
    shop = models.ForeignKey("Shops", on_delete=models.PROTECT, verbose_name="Магазины")
