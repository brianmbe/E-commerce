from django.urls import path
from .views import cart, add_to_cart, remove_cart_item, delete_cart

urlpatterns = [
    path('', cart, name='cart'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove_cart_item/<int:product_id>/',
         remove_cart_item, name='remove-cart-item'),
    path('delete_cart/<int:product_id>/', delete_cart, name='delete_cart'),
]
