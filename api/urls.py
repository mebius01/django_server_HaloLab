from django.urls import path
from .views import *
from rest_framework import routers


app_name = 'api'

urlpatterns = [
    path('category/', CategoryList.as_view(), name = 'category_list'),
    path('category/<slug:slug>', CategoryDetail.as_view(), name ='category_detail'),
    path('product/', ProductList.as_view(), name ='product_list'),
    path('product/<slug:slug>/', ProductDetail.as_view(), name='product_detail'),
]