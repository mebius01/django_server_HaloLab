from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Category, Product

class CategoryTests(APITestCase):
    def setUp(self):
        """
        Создает фейковую БД и заполняет ее данные, в тестах работает только с этой БД
        В этом конкрет реализации прав у юзера БД, на создания БД, нет!
        По этому в settings описано ...DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'...
        Это позволяет на момент тестов юзать sqlite
        """
        Category.objects.create(id          = 1,
                                name        = 'Name Category',
                                slug        = 'name_category',
                                description = 'Description for Category'
        )

        Category.objects.create(id          = 2,
                                name        = 'Name Category 2',
                                slug        = 'name_category_2',
                                description = 'Description for Category 2',
                                tree_id     = 1,
                                level       = 1,
                                parent      = Category.objects.get(id=1),
        )

        Product.objects.create(id           = 1,
                                category    = Category.objects.get(id=2),
                                name        = 'Name Product 1',
                                slug        = 'name_product_1',
                                vendor_code = 'qwerty',
                                vendor      = 'HP',
                                price       = '123.4',
                                stock       = 1,
                                available   = True,
        )

    print('Create data for DB')
    
    def test_get_data_category(self):
        # Запрос по урлу
        response = self.client.get(reverse('api:category_list'))
        # Тест падает если ответ не 200
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Тест падает если объектов чуть больше чем 1
        # По факту у нас две категории, но вторая категория есть потомком первой
        self.assertEqual(len(response.data), 1)
    
    def test_get_data_category_detail(self):
        response = self.client.get(reverse('api:category_detail', args=('name_category',)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Тест падает если полей чуть больше чем 7
        self.assertEqual(len(response.data), 7)

    def test_get_data_product(self):
        response = self.client.get(reverse('api:product_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_get_data_product_detail(self):
        response = self.client.get(reverse('api:product_detail', args=('name_product_1',)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 11)
        self.assertEqual(response.data.get('id'), 1)