from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Shops(models.Model):
    """
    Модель магазинов
    """
    name = models.CharField(max_length=20, db_index=True, verbose_name="Магазины")
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name="URL")


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop", kwargs={"shop_slug": self.slug})

    class Meta:
        verbose_name_plural = "Магазины"


class Categories(models.Model):
    """
    Модель категорий
    """
    name = models.CharField(max_length=20, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Категории"


class Products(models.Model):
    """
    Модель товаров
    """
    name = models.TextField(blank=True, db_index=True, verbose_name="Название")
    photo = models.TextField(verbose_name="Фото")
    previous_price = models.FloatField(verbose_name="Цена")
    link = models.TextField(verbose_name='Ссылка', null=True)
    cat = models.ForeignKey("Categories", on_delete=models.CASCADE, verbose_name="Категории")
    shop = models.ForeignKey("Shops", on_delete=models.CASCADE, verbose_name="Магазины")

    def get_absolute_url(self):
        return reverse('review', kwargs={'pk': self.pk})
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Продукты"


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

class ReviewModel(models.Model):
    user_id = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, null=True, blank=True)
    product_id = models.ForeignKey(Products, verbose_name='Продукт', on_delete=models.CASCADE)
    content = models.TextField(verbose_name='Текст отзыва', null=True)
    Rating = models.IntegerChoices('Rating', '1 2 3 4 5')
    rating = models.IntegerField(choices=Rating.choices, verbose_name='Рейтинг')
    date = models.DateField(verbose_name='Дата отзыва', auto_now_add=True)

    def get_absolute_url(self):
        return reverse('review', args={'product_id': self.product_id})
    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = "Отзывы"
        db_table = 'review'

