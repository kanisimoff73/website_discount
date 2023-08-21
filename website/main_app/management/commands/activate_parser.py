from bs4 import BeautifulSoup
from os import listdir
from os.path import isfile, join
from django.core.management.base import BaseCommand
from ...models import *
from website.settings import BASE_DIR
from django.core.management import call_command
from django.apps import apps
import psycopg2


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Попытка удалить таблицы командами через psycopg2
        # conn = psycopg2.connect(dbname='discount_db', user='postgres',
        #                         password='228322', host='localhost', port="5432")
        # cursor = conn.cursor()
        # print('==========================')
        #
        # removed_tables = []
        # exceptions = []
        # for model in apps.get_models():
        #     print(model.__name__)
        #     if model.__name__ in ('Shops', 'Categories', 'Products'):
        #         try:
        #             model.objects.all().delete()
        #             cursor.execute(f'DROP TABLE IF EXISTS {model._meta.db_table} CASCADE')
        #             conn.commit()
        #             print(f"Dropped table {model._meta.db_table} from model {model.__name__}")
        #         except Exception as e:
        #             exceptions.append([model._meta.db_table, str(e)])
        #             print(e)
        #             continue
        #         removed_tables.append(model._meta.db_table)
        # print(f"Removed {len(removed_tables)} tables")
        # conn.close()

        # это как будто выполняешь python manage.py flush --noinput
        # Удаляет и создаёт заного таблицы, но удаляет вообще все данные
        # Даже пользователей
        # надо найти способ удалять и заного создавать только наши таблицы
        # как вриант через команды sql всё делать, но мне кажется джанго потом будет на это ругаться, хз
        # call_command('flush', '--noinput')
        # это не пригодилось
        # call_command('migrate')

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