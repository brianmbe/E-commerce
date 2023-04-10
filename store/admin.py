from django.contrib import admin
from .models import Product

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'category', 'price',
                    'stock', 'modified_date', 'is_available']
    search_fields = ('product_name', 'category', 'stock')
    prepopulated_fields = {
        'slug': ('product_name',)
    }
