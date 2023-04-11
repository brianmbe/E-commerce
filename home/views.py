from django.shortcuts import render
from store.models import Product


# Create your views here.
def home(request):
    products = Product.objects.all().filter(is_available=True)[:8]

    context = {"products": products}
    return render(request, 'home/index.html', context)
