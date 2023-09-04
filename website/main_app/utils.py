from django.db.models import Count
from django.core.cache import cache

from .models import *
from ._menu  import menu_for_not_authenticated, menu_for_authenticated



class DataMixin:
    paginate_by = 4

    def get_user_context(self, **kwargs):
        context = kwargs
        if self.request.user.is_authenticated:
            user_menu, user_side_bar = menu_for_authenticated()
        else:
            user_menu, user_side_bar = menu_for_not_authenticated()
        context["menu"] = user_menu
        context['side_bar'] = user_side_bar
        if 'shop_selected' not in context:
            context['shop_selected'] = 0
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
