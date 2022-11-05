from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Comics
#from .models import Book


# Register your models here.
#admin.site.register(Book)


@admin.register(Comics)
class ComicsAdmin(ModelAdmin):
    pass
