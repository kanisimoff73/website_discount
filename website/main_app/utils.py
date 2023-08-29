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
side_bar = []
sql_res = Products.objects.select_related('cat', 'shop').distinct().values('shop__name', 'shop__slug', 'cat__name', 'cat__slug').order_by('shop__name')

for raw_dictionary in sql_res:
    for ready_dictionary in side_bar:
        if raw_dictionary['shop__name'] == ready_dictionary['shop__name']:
            ready_dictionary['shop_categories'].append({'cat__name': raw_dictionary['cat__name'],
                                                        'cat__slug': raw_dictionary['cat__slug']})
            break
    else:
        side_bar.append({'shop__name': raw_dictionary['shop__name'],
                         'shop__slug': raw_dictionary['shop__slug'],
                         'shop_categories': [
                             {'cat__name': raw_dictionary['cat__name'], 'cat__slug': raw_dictionary['cat__slug']}
                         ]})


class DataMixin:
    # def __init__(self):
    #     self.request = None

    def get_user_context(self, **kwargs):
        context = kwargs

        user_menu = menu.copy()
        # if not self.request.user.is_authenticated:
        #     user_menu.pop(1)
        user_side_bar = side_bar.copy()
        context["menu"] = user_menu
        context['side_bar'] = user_side_bar
        return context
