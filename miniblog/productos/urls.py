from django.urls import path
from django.contrib.auth.decorators import login_required
from productos.views.productos_view import (
    ProductView,
    ProductCreate,
    ProductDetail,
    ProductDelete,
    ProductUpdate,
    )

from productos.views.categorias_view import(
    CategoryView,
    CategoryCreate,
    CategoryDetail,
    CategoryDelete,
    CategoryUpdate,
)

from productos.views.supplier_view import(
    SupplierView,
    SupplierCreate,
    SupplierDetail,
    SupplierDelete,
    SupplierUpdate,
)

from productos.views.product_review_view import(
    ProductReviewView,
    ProductReviewCreate,
    ProductReviewDetail,
    ProductReviewUpdate,
    ProductReviewDelete,
)


urlpatterns = [
    path(route='', view=ProductView.as_view(), name='product_list'),
    path(route='create/', view=ProductCreate.as_view(), name='product_create'),
    path(route='<int:id>/detail/', view=ProductDetail.as_view(), name='product_detail'),
    path(route='<int:id>/delete/', view=ProductDelete.as_view(), name='product_delete'),
    path(route='<int:id>/update/', view=ProductUpdate.as_view(), name='product_update'),

    path(route='category/', view=CategoryView.as_view(), name='category_list'),
    path(route='category/create', view=login_required(CategoryCreate.as_view(), login_url='login'), name='category_create'),
    path(route='category/<int:id>/detail', view=CategoryDetail.as_view(), name='category_detail'),
    path(route='category/<int:id>/delete', view=login_required(CategoryDelete.as_view(), login_url='login'), name='category_delete'),
    path(route='category/<int:id>/update', view=login_required(CategoryUpdate.as_view(), login_url='login'), name='category_update'),

    path(route='supplier/', view=SupplierView.as_view(), name='supplier_list'),
    path(route='supplier/create', view=login_required(SupplierCreate.as_view(), login_url=('login')), name='supplier_create'),
    path(route='supplier/<int:id>/detail', view=SupplierDetail.as_view(), name='supplier_detail'),
    path(route='supplier/<int:id>/delete', view=login_required(SupplierDelete.as_view(), login_url='login'), name='supplier_delete'),
    path(route='supplier/<int:id>/update', view=login_required(SupplierUpdate.as_view(), login_url='login'), name='supplier_update'),

    path(route='reviews/', view=ProductReviewView.as_view(), name='review_list'),
    path(route='reviews/create', view=login_required(ProductReviewCreate.as_view(), login_url='login'), name='review_create'),
    path(route='reviews/<int:id>/detail', view=ProductReviewDetail.as_view(), name='review_detail'),
    path(route='reviews/<int:id>/delete', view=ProductReviewDelete.as_view(), name='review_delete'),
    path(route='reviews/<int:id>/update', view=login_required(ProductReviewUpdate.as_view(), login_url='login'), name='review_update'),
] 