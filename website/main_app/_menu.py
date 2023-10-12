from .models import *
from django.core.cache import cache

menu_for_user = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'О нас', 'url_name': 'about'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'},
    {'title': 'Регистрация', 'url_name': 'register'},
]

#Версия Кирилла
def get_sidebar():
    queryset = Shops.objects.all()
    side_bar = cache.get('side_bar')
    if not side_bar:
        side_bar = []

        for shop in queryset:
            categories = Categories.objects.filter(products__shop=shop.pk).distinct()
            side_bar.append((shop, categories))
        cache.set('side_bar', side_bar, 60)
    return side_bar


#Версия Дмитрия
# def get_sidebar():
#     side_bar = []
#     sql_res = Products.objects.select_related('cat', 'shop').distinct().values('shop__name', 'shop__slug', 'cat__name', 'cat__slug').order_by('shop__name')
#
#     for raw_dictionary in sql_res:
#         for ready_dictionary in side_bar:
#             if raw_dictionary['shop__name'] == ready_dictionary['shop__name']:
#                 ready_dictionary['shop_categories'].append({'cat__name': raw_dictionary['cat__name'],
#                                                             'cat__slug': raw_dictionary['cat__slug']})
#                 break
#         else:
#             side_bar.append({'shop__name': raw_dictionary['shop__name'],
#                              'shop__slug': raw_dictionary['shop__slug'],
#                              'shop_categories': [
#                                  {'cat__name': raw_dictionary['cat__name'], 'cat__slug': raw_dictionary['cat__slug']}
#                              ]})
#     return side_bar


def menu_user(self):
    side_bar = get_sidebar()
    user_menu = menu_for_user.copy()
    if self.request.user.is_authenticated:
        user_menu[-2:] = [{'title': 'Выйти', 'url_name': 'logout'}]
    user_side_bar = side_bar.copy()
    return user_menu, user_side_bar


