from library.models import Comics
from library.serializers import ComicsSerializer
from django.test import TestCase


class ComicsSerializersTestCase(TestCase):
    def test_ok(self):
        comics_1 = Comics.objects.create(title='T1',
                                         price='300.00',
                                         author='A1')
        comics_2 = Comics.objects.create(title='T2',
                                         price='300.00',
                                         author='A2')
        data = ComicsSerializer([comics_1, comics_2], many=True).data
        print(data)
        expected_data = [
            {
                'title': 'T1,',
                'price': '300.00',
                'author': 'A1'
            },
            {
                'title': 'T2,',
                'price': '300.00',
                'author': 'A2'
            }
        ]
        self.assertEqual(expected_data, data)
