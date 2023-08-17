from django.shortcuts import render
from django.views.generic import ListView

from .models import *


class MainHomePage(ListView):
    model = Products
    template_name = "main_app/index.html"
    # context_object_name = 'products'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
