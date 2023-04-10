from django.db import models
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(null=True, blank=True)
    cat_image = models.ImageField(
        upload_to='category_img', default='category_img/1.jpg', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse("product_by_category", args=[self.slug])
