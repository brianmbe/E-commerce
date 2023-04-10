from django.contrib import admin
from .models import Category

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name']
    search_fields = ['category_name']
    list_filter = ['category_name']
    prepopulated_fields = {'slug': ['category_name']}
