from django.contrib import admin
from .models import Category, Product
from mptt.admin import MPTTModelAdmin


class CategoryAdmin(MPTTModelAdmin):
    list_display        = ['name', 'id', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(admin.ModelAdmin):
    search_fields       = ['name', 'vendor_code',]
    list_display        = ['name', 'available', 'price',]
    list_filter         = ['created', 'updated', 'available', 'category', 'vendor']
    list_editable       = ['price', 'available',]
    prepopulated_fields = {'slug': ('name','vendor_code')}


admin.site.register(Category, CategoryAdmin,)
admin.site.register(Product, ProductAdmin,)