from django.contrib import admin
from .models import *
from .models import Feedback


class ShopsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    list_display_links = ("id", "name", "slug")
    search_fields = ("name", "slug")


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    list_display_links = ("id", "name", "slug")
    search_fields = ("name", "slug")


class ProductsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "photo", "previous_price", "link", "cat", "shop")
    list_display_links = ("id", "name", "photo", "previous_price", "link", "cat", "shop")


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    """
    Админ-панель модели профиля
    """
    list_display = ('email', 'ip_address', 'user')
    list_display_links = ('email', 'ip_address')


# Register your models here.
admin.site.register(Shops, ShopsAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Products, ProductsAdmin)
