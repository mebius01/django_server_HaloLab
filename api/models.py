from django.db import models
from decimal import *
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name        = models.CharField(max_length=200, db_index=True, unique=True)
    slug        = models.SlugField(max_length=200, db_index=True, unique=True)
    description = models.TextField(blank=True)
    parent      = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        unique_together = ('parent', 'slug',)
        ordering = ('tree_id', 'name',)

    def __str__(self):
        return self.name
    
    def get_product(self):
        return list(Product.objects.filter(category=self).order_by('vendor', '-price')[:24])


class Product(models.Model):
    category    = models.ForeignKey(Category,related_name='product', on_delete=models.CASCADE, help_text='Каталог товара')
    name        = models.CharField(max_length=400, db_index=True, help_text='Название товара')
    slug        = models.SlugField(max_length=400, help_text='')
    vendor_code = models.CharField(max_length=200, unique=True, help_text='Артикул, парт номер')
    vendor      = models.CharField(max_length=200, blank=True, help_text='Производитель')
    price       = models.DecimalField(max_digits=10, decimal_places=2, blank=True, help_text='Цена входящая')
    stock       = models.PositiveIntegerField(blank=True, help_text='Остатоки', default=1)
    available   = models.BooleanField(default=True, help_text='Доступен ли к заказу')
    created     = models.DateTimeField(auto_now_add=True, help_text='дата создания')
    updated     = models.DateTimeField(auto_now=True, help_text='дата обновления')

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
    
    def __str__(self):
        return self.name

