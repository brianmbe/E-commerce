from django.db import models
from django.urls import reverse
from category.models import Category

# Create your models here.


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    # old_price = models.IntegerField()
    main_picture = models.ImageField(
        upload_to='product_mgs/', default='product_mgs/1.jpg')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=False)
    modified_date = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse("product-detail", args=[self.category.slug, self.slug])
