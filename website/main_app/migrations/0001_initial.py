# Generated by Django 4.2.4 on 2023-08-29 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, verbose_name='Категория')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Shops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, verbose_name='Магазины')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, db_index=True, verbose_name='Название')),
                ('photo', models.TextField(verbose_name='Фото')),
                ('previous_price', models.FloatField(verbose_name='Цена')),
                ('link', models.TextField(null=True, verbose_name='Ссылка')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.categories', verbose_name='Категории')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.shops', verbose_name='Магазины')),
            ],
        ),
    ]
