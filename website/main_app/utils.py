from django.db.models import Count
from django.core.cache import cache

from .models import *

menu = [
    {'title': 'Домой', 'url_name': 'home'},
    {'title': 'О нас', 'url_name': 'about'},
    # {'title': 'Контакты', 'url_name': 'contact'},
    # {'title': 'Войти', 'url_name': 'login'},
    # {'title': 'Регистрация', 'url_name': 'register'},
]


class DataMixin:
    paginate_by = 4
    def get_user_context(self, **kwargs):
        context = kwargs
        user_menu = menu.copy()
        context['menu'] = user_menu
        return context