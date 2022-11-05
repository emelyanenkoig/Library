import social_django
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
import library.views
from library.views import *
from djoser import urls
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'comics', ComicsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),  # Админка
    re_path('', include('social_django.urls', namespace='social')),
    path('auth/', auth),
]

urlpatterns += router.urls
