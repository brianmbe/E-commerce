from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include('home.urls')),
    path("admin/", admin.site.urls),
    path("category/", include('category.urls')),
    path("store/", include('store.urls')),
    path("cart/", include('carts.urls')),
    # path("account/", include('account.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
