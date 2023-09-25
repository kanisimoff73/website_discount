from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.views.generic import CreateView, ListView
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView

from .email import send_contact_email_message
from .forms import RegisterUserForm, LoginUserForm, ContactForm, UserForgotPasswordForm, UserSetNewPasswordForm, ReviewForm
from .models import *
from .utils import *

class MainHomePage(DataMixin, ListView):
    model = Products
    template_name = "main_app/content.html"
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(title='Домашняя страница')
        return dict(list(context.items()) + list(user_context.items()))

    def get_queryset(self):
        return Products.objects.select_related('cat', 'shop').order_by('previous_price')

class AboutUs(DataMixin, ListView):
    model = Products
    template_name = 'main_app/about.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(title='О нас')
        return dict(list(context.items()) + list(user_context.items()))


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'main_app/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(user_context.items()))

    def get_success_url(self):
        return reverse_lazy('home')


class ShopChoice(DataMixin, ListView):
    model = Products
    template_name = 'main_app/content.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            s = Shops.objects.get(slug=self.kwargs['shop_slug'])
            user_context = self.get_user_context(title='Магазин - ' + str(s.name),
                                          shop_selected=s.slug)
        except:
            user_context = self.get_user_context()
        return dict(list(context.items()) + list(user_context.items()))

    def get_queryset(self):
        return Products.objects.filter(shop__slug=self.kwargs['shop_slug']).select_related('shop', 'cat').order_by('previous_price')

class CatigoryChoise(DataMixin, ListView):
    model = Products
    template_name = 'main_app/content.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            s = Shops.objects.get(slug=self.kwargs['shop_slug'])
            c = Categories.objects.get(slug=self.kwargs['cat_slug'])
            user_context = self.get_user_context(title=f'{s.name} - {c.name}',
                                                 shop_selected=s.slug,
                                                 cat_selected=c.slug)
        except:
            user_context = self.get_user_context()
        return dict(list(context.items()) + list(user_context.items()))


    def get_queryset(self):
        return Products.objects.filter(shop__slug=self.kwargs['shop_slug'], cat__slug=self.kwargs['cat_slug']).select_related('shop', 'cat').order_by('previous_price')


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'main_app/register.html'
    success_url = 'home'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(user_context.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

@login_required
def logout_user(request):
    logout(request)
    return redirect('home')


class UserForgotPasswordView(DataMixin, SuccessMessageMixin, PasswordResetView):
    """
    Представление по сбросу пароля по почте
    """
    form_class = UserForgotPasswordForm
    template_name = 'main_app/user_password_reset.html'
    success_message = 'Письмо с инструкцией по восстановлению пароля отправлена на ваш email'
    subject_template_name = 'main_app/email/password_subject_reset_mail.txt'
    email_template_name = 'main_app/email/password_reset_mail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(user_context.items()))

    def get_success_url(self):
        return reverse_lazy('home')


class UserPasswordResetConfirmView(DataMixin, SuccessMessageMixin, PasswordResetConfirmView):
    """
    Представление установки нового пароля
    """
    form_class = UserSetNewPasswordForm
    template_name = 'main_app/user_password_set_new.html'
    success_url = reverse_lazy('home')
    success_message = 'Пароль успешно изменен. Можете авторизоваться на сайте.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(user_context.items()))


class ContactFormView(DataMixin, SuccessMessageMixin, CreateView):
    model = Feedback
    form_class = ContactForm
    success_message = 'Ваше письмо успешно отправлено администрации сайта'
    template_name = 'main_app/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(title="Контактная форма")
        return dict(list(context.items()) + list(user_context.items()))

    def form_valid(self, form):
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.ip_address = get_client_ip(self.request)
            if self.request.user.is_authenticated:
                feedback.user = self.request.user
            send_contact_email_message(feedback.subject, feedback.email, feedback.content, feedback.ip_address, feedback.user_id)
        return super().form_valid(form)

#Можно просто кварисет определить в MainHomePage и ен делать эту view, но не знаю как лучше
class SearchStringView(DataMixin, ListView):
    model = Products
    template_name = "main_app/content.html"
    context_object_name = 'products'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=f"Результат поиска: {self.request.GET.get('search')}")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        search = None
        queryset = Products.objects.select_related('cat', 'shop').order_by('previous_price')
        form = SearchStringForm(self.request.GET or None)
        if form.is_valid():
            search = form.cleaned_data.get('search')
        if search:
            queryset_name = queryset.filter(name__icontains=search)
            if queryset_name:
                return queryset_name
            queryset = queryset.filter(cat__name__icontains=search)
        return queryset


class ProductReview(DataMixin, ListView, CreateView):
    object = None
    model = ReviewModel
    template_name = 'main_app/review_product.html'
    context_object_name = 'review'
    form_class = ReviewForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        product = Products.objects.get(id=self.kwargs['pk'])
        user_context = self.get_user_context(title=f"{product.name}",
                                             product=product)
        return dict(list(context.items()) + list(user_context.items()))

    def get_queryset(self):
        return self.model.objects.filter(product_id=self.kwargs['pk']).order_by('date')

    def form_valid(self, form):
        if form.is_valid():
            date_review = form.save(commit=False)
            date_review.product_id_id = self.kwargs['pk']
            if self.request.user.is_authenticated:
                date_review.user_id = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('review', kwargs={'pk': self.kwargs['pk']})

