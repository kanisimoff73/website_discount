from django.test import TestCase

from main_app.forms import RegisterUserForm


class RegisterUserFormTest(TestCase):
    """
    Тестирование формы регистрации пользователей
    """
    def test_availability_of_fields(self):
        """Проверка наличия всех полей"""
        fields = RegisterUserForm().fields
        for field in fields:
            self.assertIn(field, ['username', 'email', 'password1', 'password2'])

    def test_clean_username(self):
        """Проверка валидатора clean_username"""
        form_data = {
            'username': 'qwerty',
            'email': 'toxic789@mail.ru',
            'password1': '123QWE098dcv',
            'password2': '123QWE098dcv'
        }
        form = RegisterUserForm(data=form_data)
        print(form.errors['username'])
        self.assertIn('Имя qwerty', form.errors['username'])
        self.assertFalse(form.is_valid())