from django.urls import path
from .views import *

# Имя приложение + Имя пути формируют урл в темплее ref="{% url 'api:category_list' %}
# Конкретно в этом  API не критично, но в тестах урлы сформированы по этому принципу
app_name = 'api'

# урл паттерн принимает модель урла, Въю, необязательное имя
urlpatterns = [ 
    path('category/', CategoryList.as_view(), name = 'category_list'),
    path('category/<slug:slug>', CategoryDetail.as_view(), name ='category_detail'),
    path('product/', ProductList.as_view(), name ='product_list'),
    path('product/<slug:slug>/', ProductDetail.as_view(), name='product_detail'),
]