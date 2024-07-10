from typing import (
    List,
    Optional,
)

from productos.models import (
    ProductReview,
)

from productos.repositories.productosRepository import ProductosRepository

from django.contrib.auth.models import User


class ReviewRepository:
    def get_all(self) -> List[ProductReview]:
        return ProductReview.objects.all()
    
    def get_by_id(self, id) -> ProductReview:
        return ProductReview.objects.get(id = id)

    def create(self,
               producto_id: int,
               user: User,
               opinion: str,
               rating: int) -> None:
        repoProductos = ProductosRepository()
        producto = repoProductos.get_by_id(id=producto_id)
        review = ProductReview.objects.create(
            product = producto,
            author = user,
            text = opinion,
            rating = rating
        )
        return review
    
    def delete(self, review: ProductReview):
            review.delete()