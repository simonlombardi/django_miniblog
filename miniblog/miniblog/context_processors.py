from django.core.cache import cache

from productos.models import Productos, Category

def all_names_product(request):
    products = cache.get('products')
    if products == None:
        products = Productos.objects.all().values_list('name')
        cache.set('products', products, 36000)
    return {'names':products}


def all_names_category(request):
    categories = Category.objects.all()
    names = [category.name for category in categories]
    return dict(
        names_category=names
    )