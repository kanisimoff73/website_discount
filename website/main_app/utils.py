from .forms import SearchStringForm
from .models import *
from ._menu  import menu_user






class DataMixin:
    """
    Формирование контекста для меню и боковой панели
    """
    paginate_by = 10

    def get_user_context(self, **kwargs):
        context = kwargs
        user_menu, user_side_bar = menu_user(self)
        context["menu"] = user_menu
        context['side_bar'] = user_side_bar
        if 'shop_selected' not in context:
            context['shop_selected'] = 0
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        #
        #вынести во вью или оставить тут?
        search_field = SearchStringForm(self.request.GET or None)
        context['search_field'] = search_field
        #
        return context


def get_client_ip(request):
    """
    Получает IP пользователя
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    ip = x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')
    return ip