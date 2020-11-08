from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from .models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    children = serializers.ListField(read_only=True, source='get_descendants', child=RecursiveField()) 
    class Meta:
        model = Category
        fields = ['id','name','slug','tree_id','level','parent','children']
