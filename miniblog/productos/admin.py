from django.contrib import admin
from django.utils.html import format_html

# Register your models here.

from productos.models import(
    Category,
    Productos,
    ProductImage,
)

@admin.register(Category)
class CategoriasAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Productos)
class ProductosAdmin(admin.ModelAdmin):
    ordering = ('name', 'price',)
    search_fields = ('price', 'name', 'category__name',)
    list_filter = ('category',)
    readonly_fields = ('name',)
    empty_value_display = 'Aun no tiene descripcion'

    list_display = ('name',
                    'price',
                    'description',
                    'category',
                    'get_price_range',
                    'get_stock',
                    'get_total'
                    )
    
    def get_total(self, object):
        return object.price * object.stock
    def get_stock(self, object):
        POCO = '#FF0000'
        MUCHO = '#008F39'
        ESCASO = '#FFD300'
        codigo = ''
        if object.stock < 1:
            codigo = POCO
        elif 1 <= object.stock < 4:
            codigo = ESCASO
        elif 3 < object.stock < 6:
            codigo = MUCHO
        return format_html(
            '<span style="color: {}">{}</span>', codigo, object.stock
        )
    fieldsets = [(
        "informacion del producto",
        {
            "fields" : ["name", "price"],
        },
        ),
        (
            "mas informacion del producto",
            {
                "classes" : ["collapse"],
                "fields" : ["description", "stock"],
            }
            
        ),
    ]

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'image', 'description']
