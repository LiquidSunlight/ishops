# Generated by Django 2.0.2 on 2018-03-17 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name'], 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='productimage',
            options={'ordering': ['product'], 'verbose_name': 'Изображение товара', 'verbose_name_plural': 'Изображения товаров'},
        ),
    ]