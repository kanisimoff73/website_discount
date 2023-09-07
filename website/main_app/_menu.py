from .models import *

menu_not_authenticated = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'О нас', 'url_name': 'about'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'},
    {'title': 'Регистрация', 'url_name': 'register'},
]

menu_is_authenticated = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'О нас', 'url_name': 'about'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Выйти', 'url_name': 'logout'},
]
#Версия Кирилла
# queryset = Shops.objects.all()
#
# side_bar = []
#
# for shop in queryset:
#     categories = Categories.objects.filter(products__shop=shop.pk).distinct()
#     side_bar.append((shop, categories))

#Версия Дмитрия
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

def menu_for_authenticated():
    user_side_bar = side_bar.copy()
    user_menu = menu_is_authenticated.copy()
    return user_menu, user_side_bar

def menu_for_not_authenticated():
    user_side_bar = side_bar.copy()
    user_menu = menu_not_authenticated.copy()
    return user_menu, user_side_bar