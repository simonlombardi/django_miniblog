from typing import (
    List,
    Optional,
)

from productos.models import (
    Productos,
    Category
)

class CategoriasRepository:
    def get_all(self) -> List[Category]:
        return Category.objects.all()
    
    def create(self, nombre:str) -> Category.objects:
        return Category.objects.create(name = nombre)
    
    def delete(self, categoria: Category):
        categoria.delete()

    def get_by_id(self, id: int) -> Category.objects:
        return Category.objects.get(id=id)
    
    def update(self,
               categoria: Category,
               nombre: str,) -> Category.objects:
        categoria.name = nombre
        categoria.save()