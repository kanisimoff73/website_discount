from django.test import TestCase

from main_app.models import Shops


class TestModelShops(TestCase):
    """
    Тесты для модели Shops
    """
    @classmethod
    def setUpTestData(cls):
        """Создаём неизменяемы тестовые данные для БД"""
        Shops.objects.create(name='DNS-shop', slug='DNS-shop')

    def test_name_label(self):
        """
        Проверяем поле name
        """
        dns = Shops.objects.get(id=1)
        self.assertEqual(dns.name, 'DNS-shop')
        dns_vebose = dns._meta.get_field("name").verbose_name
        self.assertEqual(dns_vebose, 'Магазины')

    def test_name_max_length(self):
        """
        Проверка максимальной длинны поля name
        """
        dns = Shops.objects.get(id=1)._meta.get_field("name")
        max_length = dns.max_length
        self.assertEqual(max_length, 20)

    def test_get_absolute_url(self):
        """
        Проверяем работу get_absolute_url
        """
        dns = Shops.objects.get(id=1)
        self.assertEqual(dns.get_absolute_url(), '/DNS-shop/')

    def test_slug_label(self):
        """
        Проверяем поле name
        """
        dns = Shops.objects.get(id=1)
        self.assertEqual(dns.slug, 'DNS-shop')
        dns_vebose = dns._meta.get_field("slug").verbose_name
        self.assertEqual(dns_vebose, 'URL')

    def test_slug_max_length(self):
        """
        Проверка максимальной длинны поля name
        """
        dns = Shops.objects.get(id=1)._meta.get_field("slug")
        max_length = dns.max_length
        self.assertEqual(max_length, 200)
