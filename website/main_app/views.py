from django.views.generic import CreateView, FormView, ListView
from django.contrib.auth.views import LoginView
from .utils import *


class MainHomePage(DataMixin, ListView):
    template_name = "main_app/home.html"


class ProductsView(DataMixin, ListView):
    template_name = "main_app/home.html"
    context_object_name = "products"

    def get_queryset(self):
        return Products.objects.filter(cat__slug=self.kwargs["cat_slug"])


class AboutUs(DataMixin, ListView):
    template_name = 'main_app/about.html'


class ContactFormView(DataMixin, FormView):
    template_name = 'main_app/contact.html'


class LoginIn(DataMixin, LoginView):
    template_name = 'main_app/login_in.html'


class RegisterUser(DataMixin, CreateView):
    template_name = 'main_app/register.html'
