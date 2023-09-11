from bs4 import BeautifulSoup
from os import listdir
from os.path import isfile, join
from django.core.management.base import BaseCommand
from ...models import *
from website.settings import BASE_DIR
from django.core.management import call_command
from django.apps import apps
import psycopg2
from transliterate import translit, get_available_language_codes
from os.path import exists
from unidecode import unidecode
from ._parser_command import refresh_tables

no_photo = '\static\main_app\images\lily-grasso-karlach.jpg'
class Command(BaseCommand):

    def handle(self, *args, **options):
        """
        Удаление созданных нами таблиц и обратное их добавление,
        что бы id(pk) всегда формировался с 1, с последующим наполнением таблиц данными
        """

        refresh_tables() # Обнуляем данные в таблицах
        #Парсим наши данные
        data_dir = join(BASE_DIR, 'main_app\static\main_app\data')
        photo_dir = '\static\main_app\data'
        shops_id = {}
        categories_id = {}
        shop_id = 1
        cat_id = 1

        for shop_name in listdir(data_dir):
            for cat in listdir(join(data_dir, shop_name)):
                onlyfiles = [f for f in listdir(join(data_dir, shop_name, cat)) if
                             isfile(join(data_dir, shop_name, cat, f))]
                if onlyfiles:
                    if shop_name not in shops_id:
                        Shops.objects.create(name=shop_name, slug=shop_name)  # создаем магазин если его ещё нет
                        shops_id[shop_name] = shop_id
                        shop_id += 1
                    if cat not in categories_id:
                        categories_id[cat] = cat_id
                        cat_id += 1
                        cat_slug = translit(cat, 'ru', reversed=True).lower()
                        rep = [',', ' ', '-', "\'"]
                        for symbol in rep:
                            if symbol in cat_slug:
                                cat_slug = cat_slug.replace(symbol, '')
                        Categories.objects.create(name=cat, slug=cat_slug)  # создаем категорию если её еще нет
                    cat_id_ = categories_id[cat]
                    shop = shops_id[shop_name]
                for file_name in onlyfiles:
                    path_to_file = join(data_dir, shop_name, cat, file_name)
                    with open(path_to_file, encoding='utf-8') as file:
                        src = file.read()
                    soup = BeautifulSoup(src, 'lxml')
                    print(path_to_file)

                    if shop_name == 'DNS-shop':
                        all_products_data = soup.find_all(class_='catalog-product')
                        for item in all_products_data:
                            name = item.find(class_='catalog-product__name').text[:-1]
                            photo = item.find('picture').find('img').get('src')[2:]
                            if photo:
                                path_to_photo = join(data_dir, shop_name, cat, photo)
                                path_to_photo_for_site = join(photo_dir, shop_name, cat, photo)
                                if not exists(path_to_photo):
                                    path_to_photo_for_site = no_photo
                            else:
                                path_to_photo_for_site = no_photo
                            previous_price = int(
                                item.find_next(class_='product-buy__price_active').next_element[:-1].rstrip().replace(
                                    ' ', ''))
                            link = item.find(class_='catalog-product__name').get('href')
                            Products.objects.create(
                                name=name,
                                photo=path_to_photo_for_site,
                                previous_price=previous_price,
                                link=link,
                                cat_id=cat_id_,
                                shop_id=shop,
                            )

                    if shop_name == 'Mvideo':
                        rows = True
                        all_products_data = soup.find_all('div', {'class': 'product-cards-row'})
                        if not all_products_data:
                            all_products_data = soup.find_all('div', {'class': 'product-cards-layout__item'})
                            rows = False
                        for item in all_products_data:
                            if rows:
                                products_rows = item.find_all(class_='product-title__text')
                                for row in products_rows:
                                    name = row.text
                                    photo = row.find_previous('img').get('src')[2:]
                                    if photo:
                                        path_to_photo = join(data_dir, shop_name, cat, photo)
                                        path_to_photo_for_site = join(photo_dir, shop_name, cat, photo)
                                        if not exists(path_to_photo):
                                            path_to_photo_for_site = no_photo
                                    else:
                                        path_to_photo_for_site = no_photo
                                    price = int(''.join(map(str, list(
                                        i for i in (unidecode(row.find_next(class_='price__main-value').text)) if
                                        i.isdigit()))))
                                    if not price:
                                        price = 999999
                                    link = row.get('href')
                                    Products.objects.create(
                                        name=name,
                                        photo=path_to_photo_for_site,
                                        previous_price=price,
                                        link=link,
                                        cat_id=cat_id_,
                                        shop_id=shop,
                                    )
                            else:
                                name = item.find(class_='product-title__text').text
                                photo = item.find('picture').find('img').get('src')[2:]
                                if photo:
                                    path_to_photo = join(data_dir, shop_name, cat, photo)
                                    path_to_photo_for_site = join(photo_dir, shop_name, cat, photo)
                                    if not exists(path_to_photo):
                                        path_to_photo_for_site = no_photo
                                else:
                                    path_to_photo_for_site = no_photo
                                price = item.find('span', {'class': 'price__main-value'})
                                if price:
                                    price = int(
                                        ''.join(map(str, list(i for i in (unidecode(price.text)) if i.isdigit()))))
                                else:
                                    price = 999999
                                link = item.find(class_='product-title__text').get('href')
                                Products.objects.create(
                                    name=name,
                                    photo=path_to_photo_for_site,
                                    previous_price=price,
                                    link=link,
                                    cat_id=cat_id_,
                                    shop_id=shop,
                                )

                    if shop_name == 'Eldorado':
                        all_products_data = (soup.find("div", id="listing-container").find("ul", class_="Yk").
                                             find_all("li", class_="kD"))
                        for item in all_products_data:
                            name = item.find("a", class_="tD").text
                            photo = item.find("a", class_="Bm").next_element.get("src")[2:]
                            if photo:
                                path_to_photo = join(data_dir, shop_name, cat, photo)
                                path_to_photo_for_site = join(photo_dir, shop_name, cat, photo)
                                if not exists(path_to_photo):
                                    path_to_photo_for_site = no_photo
                            else:
                                path_to_photo_for_site = no_photo
                            price = int("".join(
                                map(str, list(
                                    i for i in (unidecode(item.find("span", class_="ZG gH").text)) if i.isdigit()))))
                            link = item.find("div", class_="lD nD").find("a").get("href")
                            Products.objects.create(
                                name=name,
                                photo=path_to_photo_for_site,
                                previous_price=price,
                                link=link,
                                cat_id=cat_id_,
                                shop_id=shop,
                            )

                    if shop_name == 'Citilink':
                        all_products_data = soup.find_all("div", class_="e12wdlvo0 app-catalog-1bogmvw e1loosed0")
                        for item in all_products_data:
                            name = "".join(
                                item.find("div", class_="app-catalog-1tp0ino e1an64qs0").find("a").text.split(",")[:-1])
                            photo = item.find("div", class_="app-catalog-lxji0k e153n9o30")
                            if photo is None:
                                photo = no_photo
                            else:
                                photo = item.find("div", class_="app-catalog-lxji0k e153n9o30").next_element.get("src")[
                                        2:]
                            if photo:
                                path_to_photo = join(data_dir, shop_name, cat, photo)
                                path_to_photo_for_site = join(photo_dir, shop_name, cat, photo)
                                if not exists(path_to_photo):
                                    path_to_photo_for_site = no_photo
                            else:
                                path_to_photo_for_site = no_photo
                            price = int("".join(
                                map(str, list(i for i in (unidecode(item.find("span", class_="e1j9birj0 e106ikdt0 "
                                                                                             "app-catalog-j8h82j "
                                                                                             "e1gjr6xo0").text)) if
                                              i.isdigit()))))
                            link = item.find("div", class_="app-catalog-1tp0ino e1an64qs0").find("a").get("href")
                            Products.objects.create(
                                name=name,
                                photo=path_to_photo_for_site,
                                previous_price=price,
                                link=link,
                                cat_id=cat_id_,
                                shop_id=shop,
                            )
