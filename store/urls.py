from django.urls import path
from .views import store, product_detail, search

urlpatterns = [
    path('', store, name='store'),
    path('category/<slug:category_slug>/', store, name='product_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/',
         product_detail, name='product-detail'),
    path('search/', search, name='search')
]
