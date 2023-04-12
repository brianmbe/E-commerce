from django.contrib import admin
from .models import Product, Variation

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'category', 'price',
                    'stock', 'modified_date', 'is_available']
    search_fields = ('product_name', 'category', 'stock')
    prepopulated_fields = {
        'slug': ('product_name',)
    }


@admin.register(Variation)
class VariationAdmin(admin.ModelAdmin):
    list_display = ['product', 'variation_category', 'variation_value',
                    'is_active']
    list_filter = ['product', 'variation_category', 'variation_value']
    search_fields = ('product', 'variation_category',)
    list_editable = ["is_active"]
