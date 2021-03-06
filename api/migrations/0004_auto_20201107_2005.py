# Generated by Django 3.0.8 on 2020-11-07 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20201107_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='description_uk',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(db_index=True, max_length=200, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_uk',
            field=models.CharField(db_index=True, max_length=200, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_ru',
            field=models.TextField(blank=True, help_text='Описание товара', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_uk',
            field=models.TextField(blank=True, help_text='Описание товара', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_ru',
            field=models.CharField(db_index=True, help_text='Название товара', max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_uk',
            field=models.CharField(db_index=True, help_text='Название товара', max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='specifications_ru',
            field=models.TextField(blank=True, help_text='Характеристики товара', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='specifications_uk',
            field=models.TextField(blank=True, help_text='Характеристики товара', null=True),
        ),
    ]
