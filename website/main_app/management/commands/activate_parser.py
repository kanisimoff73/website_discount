from bs4 import BeautifulSoup
from os import listdir
from os.path import isfile, join
from django.core.management.base import BaseCommand
from ...models import *
from website.settings import BASE_DIR


class Command(BaseCommand):

    def handle(self, *args, **options):
        #
        #Попробовать тут удалять данные из БД
        data_dir = join(BASE_DIR, 'main_app\static\main_app\data')
        shops_id = {}
        categories_id = {}

        for shop_id, shop_name in enumerate(listdir(data_dir)):
            shops_id[shop_name] = shop_id + 1
            # Shops.objects.create(name=shop_name)

            for cat_id, dir in enumerate(listdir(join(data_dir, shop_name))):
                if dir not in categories_id:
                    categories_id[dir] = cat_id + 1
                # Categories.objects.create(name=dir)
                onlyfiles = [f for f in listdir(join(data_dir, shop_name, dir)) if isfile(join(data_dir, shop_name, dir, f))]
                # for file_name in onlyfiles:
                #     path_to_file = join(data_dir, dir, file_name)
                #     with open(path_to_file, encoding='utf-8') as file:
                #         src = file.read()
                #
                #     soup = BeautifulSoup(src, 'lxml')
                #     domen_name = 'https://www.dns-shop.ru'
                #
                #     all_products_href = soup.find_all(class_='catalog-product__name')
                #     for item in all_products_href:
                #         name = item.text[:-1]
                #         href = item.get('href')
                #         print(name, href)
                #         # Products.objects.create(
                #         #     name=,
                #         #     price=,
                #         #     shop_id=shop_id[shop_name])