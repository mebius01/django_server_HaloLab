# basic import
from .serializers import ProductSerializer, CategorySerializer
from .models import Category, Product
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.conf import settings

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 24
    page_size_query_param = 'page_size'
    max_page_size = 10


class ProductList(ListAPIView):
    queryset = Product.objects.all().order_by('vendor', '-price',)
    serializer_class = ProductSerializer
    pagination_class = LargeResultsSetPagination

    @method_decorator(cache_page(settings.CACHE_TTL))
    def dispatch(self, *args, **kwargs):
        return super(ProductList, self).dispatch(*args, **kwargs)


class ProductDetail(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    
    @method_decorator(cache_page(settings.CACHE_TTL))
    def dispatch(self, *args, **kwargs):
        return super(ProductDetail, self).dispatch(*args, **kwargs)


class CategoryList(ListAPIView):
    queryset = Category.objects.root_nodes().order_by('tree_id')
    serializer_class = CategorySerializer
    
    @method_decorator(cache_page(30*2))
    def dispatch(self, *args, **kwargs):
        return super(CategoryList, self).dispatch(*args, **kwargs)


class CategoryDetail(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    
    @method_decorator(cache_page(15))
    def dispatch(self, *args, **kwargs):
        return super(CategoryDetail, self).dispatch(*args, **kwargs)

