from django.contrib import admin
from .models import *


@admin.register(Shops)
class ShopsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    list_display_links = ("id", "name", "slug")
    search_fields = ("name", "slug")


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    list_display_links = ("id", "name", "slug")
    search_fields = ("name", "slug")


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "photo", "previous_price", "link", "cat", "shop")
    list_display_links = ("id", "name", "photo", "previous_price", "link", "cat", "shop")
    search_fields = ("id", "name", "cat__name", "shop__name")


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    """
    Админ-панель модели профиля
    """
    list_display = ('email', 'ip_address', 'user')
    list_display_links = ('email', 'ip_address')

    
@admin.register(ReviewModel)
class ReviewAdmin(admin.ModelAdmin):
    """
    Админ-панель модели обзоров
    """
    list_display = ("id", "content", "rating", "date", "product_id", "user_id")
    list_display_links = ("content", "rating")
    search_fields = ("rating", "product_id__name")

