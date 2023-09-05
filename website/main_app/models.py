from django.contrib.auth.models import User
from django.db import models


class Shops(models.Model):
    """
    Модель магазинов
    """
    objects = None
    name = models.CharField(max_length=20, db_index=True, verbose_name="Магазины")
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name="URL")

    # class Meta:
    #     db_table = 'shops'

class Categories(models.Model):
    """
    Модель категорий
    """
    objects = None
    name = models.CharField(max_length=20, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name="URL")


class Products(models.Model):
    """
    Модель товаров
    """
    objects = None
    name = models.TextField(blank=True, db_index=True, verbose_name="Название")
    photo = models.TextField(verbose_name="Фото")
    previous_price = models.FloatField(verbose_name="Цена")
    link = models.TextField(verbose_name='Ссылка', null=True)
    cat = models.ForeignKey("Categories", on_delete=models.CASCADE, verbose_name="Категории")
    shop = models.ForeignKey("Shops", on_delete=models.CASCADE, verbose_name="Магазины")


class Feedback(models.Model):
    """
    Модель обратной связи
    """
    subject = models.CharField(max_length=255, verbose_name='Тема письма')
    email = models.EmailField(max_length=255, verbose_name='Email')
    content = models.TextField(verbose_name='Содержимое письма')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')
    ip_address = models.GenericIPAddressField(verbose_name='IP отправителя', blank=True, null=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
        ordering = ['-time_create']
        db_table = 'feedback'

    def __str__(self):
        return f'Вам письмо от {self.email}'
