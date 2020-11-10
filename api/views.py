# Импорт моделей и сериализаторов 
from .serializers import ProductSerializer, CategorySerializer
from .models import Category, Product
# Импорт встроенных классов из DRF
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
# Импорты необходимы для  кеширование 
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.conf import settings


# Класс DRF отвечает за пагинацию 
class LargeResultsSetPagination(PageNumberPagination):
    page_size = 24
    page_size_query_param = 'page_size'
    max_page_size = 10


class ProductList(ListAPIView):
    """
    Класс наследует базовый класс DRF ListAPIView Отвечает за отображение списка
    """
    queryset = Product.objects.all().order_by('vendor', '-price',)
    serializer_class = ProductSerializer
    pagination_class = LargeResultsSetPagination

    @method_decorator(cache_page(settings.CACHE_TTL))
    """
    Декоратор, принимает метод из кеша, который принимает значение, type = int, время жизни кеша
    В этом методе реализован импорт глобального значения из settings
    """
    def dispatch(self, *args, **kwargs):
        return super(ProductList, self).dispatch(*args, **kwargs)


class ProductDetail(RetrieveAPIView):
    """
    Класс наследует базовый класс DRF RetrieveAPIView Отвечает за вывод конкретного элемента по ключу

    Метод lookup_field = 'slug' это есть сам ключ, может использовать любой уникальный идентификатор объекта типа id. Этот параметр прилетает из url
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    
    @method_decorator(cache_page(settings.CACHE_TTL))
    def dispatch(self, *args, **kwargs):
        return super(ProductDetail, self).dispatch(*args, **kwargs)


class CategoryList(ListAPIView):
    # Queryset принимает не всю категорию, а только root и в цепочке сортирует
    # Это необходимо, чтобы удалить из выдачи не корневые объекты
    # так как корневые уже содержат потомков
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

