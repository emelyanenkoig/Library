from django.db import models
from django.contrib.auth.models import User


# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField(max_length=1000)
#     author = models.CharField(max_length=100)
#     pages = models.CharField(max_length=100)
#     year = models.CharField(max_length=5)
#     user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
#     cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
#
#     def __str__(self):
#         return self.title
#
#
# class Category(models.Model):
#     name = models.CharField(max_length=100, db_index=True)
#
#     def __str__(self):
#         return self.title


class Comics(models.Model):
    title = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    author = models.CharField(max_length=250)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.title}'