from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm

from .models import Feedback, ReviewModel


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data['username']
        if username == 'qwerty':
            raise ValidationError('Имя qwerty', code='invalid')

        return username


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class UserForgotPasswordForm(PasswordResetForm):
    """
    Запрос на восстановление пароля
    """
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))



class UserSetNewPasswordForm(SetPasswordForm):
    """
    Изменение пароля пользователя после подтверждения
    """
    new_password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class ContactForm(forms.ModelForm):
    """
    Форма отправки обратной связи
    """
    class Meta:
        model = Feedback
        fields = ('subject', 'email', 'content')

        widgets = {
            'subject': forms.TextInput(attrs={'class': 'subject-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }


class SearchStringForm(forms.Form):
    search = forms.CharField(label='поиск', widget=forms.TextInput(attrs={'class': 'search-field',
                                                                          'placeholder': 'введите запрос'}))


class ReviewForm(forms.ModelForm):
    """
    Форма для комментария
    """
    class Meta:
        model = ReviewModel
        fields = ('content', 'rating')

        widgets = {
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10, 'class': 'review-content'}),
            'rating': forms.Select(attrs={'class': 'review-choice'})
        }