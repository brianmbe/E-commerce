from .models import Category


def menu_links(reuest):
    links = Category.objects.all()
    return dict(category_links=links)
