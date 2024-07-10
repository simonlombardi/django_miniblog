from typing import (
    List,
    Optional,
)

from productos.models import (
    Supplier    
)

class SupplierRepository:
    def get_all(self) -> List[Supplier]:
        return Supplier.objects.all()
    
    def create(self,
            nombre: str,
            direccion: str,
            telefono: int,) -> Supplier.objects:
        return Supplier.objects.create(name = nombre,
                                       address = direccion,
                                       phone = telefono)
    
    def delete(self,
               supplier: Supplier):
        supplier.delete()

    def get_by_id(self,
                  id: int) -> Supplier.objects:
        return Supplier.objects.get(id=id)
    
    def update(self,
               proveedor: Supplier,
               nombre: str,
               direccion: str,
               telefono: int,) -> Supplier.objects:
        proveedor.name = nombre
        proveedor.address = direccion
        proveedor.phone = telefono

        proveedor.save()