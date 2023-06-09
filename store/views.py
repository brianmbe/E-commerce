from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .models import Product
from category.models import Category
from carts.models import CartItem
from carts.views import _cart_id
from django.http import HttpResponse

# Create your views here.


def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.all().filter(category=categories, is_available=True)
        paginator = Paginator(products, 9)
        page = request.GET.get('page')
        paged_product = paginator.get_page(page)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        paginator = Paginator(products, 9)
        page = request.GET.get('page')
        paged_product = paginator.get_page(page)
        product_count = products.count()

    context = {
        "products": paged_product,
        "product_count": product_count
    }

    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(
            category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(
            request), product=single_product).exists()
    except Exception as err:
        raise err
    context = {
        'single_product': single_product,
        'in_cart': in_cart
    }

    return render(request, 'store/product-detail.html', context)


def search(request):
    products = None
    product_count = None
    if 'search_query' in request.GET:
        search_query = request.GET['search_query']
        if search_query:
            products = Product.objects.order_by(
                '-created_date').filter(Q(description__icontains=search_query) | Q(product_name__icontains=search_query))
            product_count = products.count()
        else:
            return redirect('store')

    context = {
        'products': products,
        'product_count': product_count
    }

    return render(request, 'store/store.html', context)
