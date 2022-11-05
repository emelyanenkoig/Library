import json

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from library.models import Comics
from library.serializers import ComicsSerializer


class ComicsAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='Test_username')
        self.comics_1 = Comics.objects.create(title='Test_comics1', price='500.00', author='A1', owner=self.user),
        self.comics_2 = Comics.objects.create(title='Test_comics2', price='400.00', author='A5', owner=self.user),
        self.comics_3 = Comics.objects.create(title='Test_comics2 A1', price='300.00', author='A2', owner=self.user)

    def test_get(self):
        url = reverse('comics-list')
        response = self.client.get(url, data={'price': 400})
        serializer_data = ComicsSerializer([self.comics_1,
                                            self.comics_2,
                                            self.comics_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_filter(self):
        url = reverse('comics-list')
        response = self.client.get(url, data={'search': 'A1'})
        serializer_data = ComicsSerializer([self.comics_1,
                                            self.comics_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_create(self):
        self.assertEqual(3, Comics.objects.all().count())
        url = reverse('comics-list')
        data = {
            "title": "Мисс Марвел",
            "price": 269.00,
            "author": "Камалла Хан"
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.post(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(4, Comics.objects.all().count())
        self.assertEqual(self.user, Comics.objects.last().owner)

    def test_update_not_owner(self):
        self.user2 = User.objects.create(username='Test_username2', is_staff=True)
        url = reverse('comics-detail', args=(self.comics_2.id,))

        data = {
            "title": self.comics_2.title,
            "price": 575,
            "author": self.comics_2.author
        }
        json_data = json.dumps(data)

        self.client.force_login(self.user2)
        response = self.client.post(url, data=json_data,
                                    content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.comics_2.refresh_from_db()
        self.assertEqual(25, self.comics_2.price)
