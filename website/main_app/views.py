from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.views import LoginView

from .models import *
from .utils import *


class MainHomePage(DataMixin, ListView):
    model = Products
    template_name = "main_app/index.html"
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Домашняя страница')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Products.objects.select_related('cat', 'shop').order_by('previous_price')

class AboutUs(DataMixin, ListView):
    model = Products
    template_name = 'main_app/about.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='О нас')
        return dict(list(context.items()) + list(c_def.items()))


class ContactFormView(DataMixin, FormView):
    template_name = 'main_app/contact.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Контакты')
        return dict(list(context.items()) + list(c_def.items()))


class LoginIn(DataMixin, LoginView):
    template_name = 'main_app/login_in.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Войти')
        return dict(list(context.items()) + list(c_def.items()))


class RegisterUser(DataMixin, CreateView):
    template_name = 'main_app/register.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))


class ShopChoice(DataMixin, ListView):
    model = Products
    template_name = 'main_app/index.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        print(self.kwargs)
        context = super().get_context_data(**kwargs)
        s = Shops.objects.get(slug=self.kwargs['shop_slug'])
        c_def = self.get_user_context(title='Магазин - ' + str(s.name),
                                      shop_selected=s.slug)
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Products.objects.filter(shop__slug=self.kwargs['shop_slug']).select_related('shop').order_by('previous_price')

class CatigoryChoise(DataMixin, ListView):
    model = Products
    template_name = 'main_app/index.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        s = Shops.objects.get(slug=self.kwargs['shop_slug'])
        c = Categories.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title=f'{s.name} - {c.name}',
                                      shop_selected=s.slug,
                                      cat_selected=c.slug)
        return dict(list(context.items()) + list(c_def.items()))


    def get_queryset(self):
        return Products.objects.filter(shop__slug=self.kwargs['shop_slug'], cat__slug=self.kwargs['cat_slug']).select_related('shop', 'cat')