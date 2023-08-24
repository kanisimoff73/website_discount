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
    def __init__(self):
        self.request = None

    def get_user_context(self, **kwargs):
        context = kwargs

        user_menu = menu.copy()
        # if not self.request.user.is_authenticated:
        #     user_menu.pop(1)

        context["menu"] = user_menu
        return context
