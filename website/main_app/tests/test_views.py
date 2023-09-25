from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class TestView(TestCase):

    def setUp(self) -> None:
        """Изменяемые данные для тестирования"""
        test_user1 = User.objects.create_user(username='Testuser1', password='12345')
        test_user1.save()

    def test_menu_for_logged_user(self):
        """Проверка меню для зарегистрированного пользователя"""
        login = self.client.login(username='Testuser1', password='12345')
        resp = self.client.get('')
        self.assertEqual(str(resp.context['user']), 'Testuser1')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('Выйти' in resp.content.decode())

    def test_home(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_dns(self):
        response = self.client.get('/DNS-shop/')
        self.assertEqual(response.status_code, 200)

