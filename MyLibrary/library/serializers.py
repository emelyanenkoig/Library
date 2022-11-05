import io
from abc import ABC

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
# from .models import Book
from .models import Comics


# class BookSerializer(serializers.ModelSerializer):
#     user = serializers.HiddenField(default=serializers.CurrentUserDefault())
#
#     class Meta:
#         model = Book
#         fields = '__all__'


class ComicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comics
        fields = '__all__'


# class BookModel:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author


# class BookSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     author = serializers.CharField(max_length=255)
#     description = serializers.CharField(max_length=1000)
#     year = serializers.CharField()
#     pages = serializers.CharField(max_length=100)
#
#     def create(self, validated_data):
#         return Book.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):  #  СЮДА ПРИХОДИТ ЗАПРОС ЧТО СТАРЫЕ ДАННЫЕ instance.title НУЖНО ЗАМЕНИТЬ НА НОВЫЕ ПРОВЕРЕННЫЕ ДАННЫЕ validated.data. ДАННЫЕ ВВОДЯТСЯ ЧЕРЕЗ get()
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.author = validated_data.get('author', instance.author)
#         instance.pages = validated_data.get('pages', instance.pages)
#         instance.year = validated_data.get('year', instance.year)
#         instance.save()
#         return instance


#  как преобразовываются данные в JSON
# def encode():
#     model = BookModel('Civil Law', 'Sukhanov')
#     model_sr = BookSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# # def decode():
# #     stream = io.BytesIO(b'{"title":"Civil Law","author":"Sukhanov"}')
# #     data = JSONParser().parse(stream)
# #     serializer = BookSerializer(data=data)
# #     serializer.is_valid()
# #     print(serializer.validated_data)
