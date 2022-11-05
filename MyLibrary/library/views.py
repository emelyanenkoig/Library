from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated, BasePermission
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Comics
# from .models import Book
from library.serializers import ComicsSerializer
# from library.serializers import BookSerializer
from rest_framework.generics import DestroyAPIView
from library.permissions import IsAdminOrReadOnly, IsOwnerOrAdminOrReadOnly, IsOwnerOrStaffOrReadOnly
from rest_framework.authtoken.models import Token
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


class BookAPIPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page_size'
    max_page_size = 10000


class ComicsViewSet(viewsets.ModelViewSet):
    queryset = Comics.objects.all()
    serializer_class = ComicsSerializer

    # Filters
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['price']
    search_fields = ['author', 'title']
    ordering_fields = ['price', 'author']

    # Permission
    permission_classes = (IsOwnerOrStaffOrReadOnly,)

    def perform_create(self, serializer):
        serializer.validated_data['owner'] = self.request.user
        serializer.save()


def auth(request):
    return render(request, 'oauth.html')






# class BookViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# class BookAPIList(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly,)
#     pagination_class = BookAPIPagination
#
#
# class BookAPIUpdate(generics.RetrieveUpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = (IsOwnerOrAdminOrReadOnly,)
#
#
# class BookAPIDestroy(generics.RetrieveDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = (IsAdminOrReadOnly,)
