from typing import (
    List,
    Optional,
)

from productos.models import (
    Productos,
    Category
)

#logger = logging.getLogger(__name__)

class ProductosRepository:
    def create(self,
               nombre: str,
               precio: float,
               cantidad: int,
               categoria: Optional[Category] = None,
               descripcion: Optional[str] = None,
               ) -> Productos.objects:
        
        return Productos.objects.create(
            name = nombre,
            description = descripcion,
            price = float(precio),
            category = categoria,
            stock = int(cantidad),
        )
    
    def update(self,
               producto: Productos,
               nombre: str,
               precio: float,
               cantidad: int,
               categoria: Optional[Category] = None,
               descripcion: Optional[str] = None,
               ) -> None:
        if int(cantidad) < 0:
            raise ValueError('El stock no puede ser menor a 0')
        if float(precio) < 0 :
            raise ValueError('El precio no puede ser menor a 0')
        
        producto.name = nombre
        producto.description = descripcion
        producto.price = float(precio)
        producto.stock = int(cantidad)
        producto.category = categoria

        producto.save()
    
    def get_all(self) -> List[Productos]:
        return Productos.objects.all()
    
    def filter_by_id(self, producto_id,) -> Optional[Productos]:
        return Productos.objects.filter(id=producto_id).first()
    
    def get_by_id(self, id: int,) -> Optional[Productos]:
        try:
            product = Productos.objects.get(id=id)
        except:
            product = None
        return product
    
    def get_product_on_price_range(
            self,
            min_price = float,
            max_price = float,
        ) -> List[Productos]:
        productos = Productos.objects.filter(
            price__range = (min_price, max_price)
        )
        return productos
    
    def filter_by_category(
            self,
            categoria = Category,
    ) -> List[Productos]:
        return Productos.objects.filter(category = categoria)
    
    def filter_by_category_name(
            self,
            categoria = str,
    ) -> List[Productos]:
        return Productos.objects.filter(category__name = categoria)

    def delete(self, producto: Productos):
        producto.delete()

    def get_product_gte_stock(self,
                              cantidad: int
                              ) -> List[Productos]:
        return Productos.objects.filter(stock__gte=cantidad)
    
    def get_product_lte_stock(self,
                              cantidad: int
                              ) -> List[Productos]:
        return Productos.objects.filter(stock__lte=cantidad)
    