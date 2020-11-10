from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from .models import Category, Product

# Сериализатор, отдает все поля объекта
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


# Сериализатор, отдает конкретные поля объекта
# Для рекурсивного добавления в поле children использует сторонний пакет
class CategorySerializer(serializers.ModelSerializer):
    children = serializers.ListField(read_only=True, source='get_descendants', child=RecursiveField()) 
    class Meta:
        model = Category
        fields = ['id','name','slug','tree_id','level','parent','children']
