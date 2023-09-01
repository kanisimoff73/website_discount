from django.db.models import Count
from django.core.cache import cache
from .models import *

menu = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'О нас', 'url_name': 'about'},
    {'title': 'Контакты', 'url_name': 'contact'},
    # {'title': 'Войти', 'url_name': 'login'},
    # {'title': 'Регистрация', 'url_name': 'register'},
]


class DataMixin:
    model = Shops
    context_object_name = "shops"

    def get_main_context(self, **kwargs):
        context = kwargs
        context["menu"] = menu
        return context

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        categories_by_shop = []

        for shop in context["shops"]:
            categories = Categories.objects.filter(products__shop=shop.pk).distinct()
            categories_by_shop.append((shop, categories))

        context["categories_by_shop"] = categories_by_shop

        main_menu = self.get_main_context()
        return dict(list(context.items()) + list(main_menu.items()))
