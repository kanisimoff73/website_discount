from django.views.generic import CreateView, FormView, ListView
from django.contrib.auth.views import LoginView
from .utils import *


class MainHomePage(DataMixin, ListView):
    template_name = "main_app/home.html"
    context_object_name = "products"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        main_menu = self.get_main_context(title='Главная страница')
        return dict(list(context.items()) + list(main_menu.items()))

    def get_queryset(self):
        return Products.objects.all()


class ProductsView(DataMixin, ListView):
    template_name = "main_app/home.html"
    context_object_name = "products"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        main_menu = self.get_main_context(title='Продукты')
        return dict(list(context.items()) + list(main_menu.items()))

    def get_queryset(self):
        return Products.objects.filter(shop__slug=self.kwargs["shop_slug"], cat__slug=self.kwargs["cat_slug"])


class ShopsView(DataMixin, ListView):
    template_name = "main_app/home.html"
    context_object_name = "products"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        main_menu = self.get_main_context(title='Магазины')
        return dict(list(context.items()) + list(main_menu.items()))

    def get_queryset(self):
        return Products.objects.filter(shop__slug=self.kwargs["shop_slug"])


class AboutUs(DataMixin, ListView):
    template_name = 'main_app/about.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        main_menu = self.get_main_context(title='О нас')
        return dict(list(context.items()) + list(main_menu.items()))


class ContactFormView(DataMixin, FormView):
    template_name = 'main_app/contact.html'


class LoginIn(DataMixin, LoginView):
    template_name = 'main_app/login_in.html'


class RegisterUser(DataMixin, CreateView):
    template_name = 'main_app/register.html'
