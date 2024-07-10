from django.views import View
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from productos.models import ProductImage
from productos.forms import ProductForm
from productos.repositories.productosRepository import ProductosRepository
from productos.repositories.categoriasRepository import CategoriasRepository

class ProductView(View):
    def get(self, request):
        repo = ProductosRepository()
        productos = repo.get_all()

        return render(
            request,
            'product/list.html',
            {
             'products': productos
            }
        )

class ProductCreate(View):
    def get(self, request):
        if request.user.is_staff:
            form = ProductForm()

            return render(
                request,
                'product/create.html',
                {
                'form': form,
                }
            )
        else:
            return redirect('product_list')
    
    def post(self, request):
        if request.user.is_staff:
            productRepo = ProductosRepository()
            categoryRepo = CategoriasRepository()
            data = request.POST

            name = data.get('name')
            description = data.get('description')
            price = data.get('price')
            categoryId = data.get('category')
            category = categoryRepo.get_by_id(id=categoryId)
            stock = data.get('stock')

            newProduct = productRepo.create(
                nombre=name,
                precio=price,
                cantidad=stock,
                categoria=category,
                descripcion=description,
            )
            
            return redirect('product_detail', newProduct.id)
        else:
            return redirect('product_list')

class ProductDetail(View):
    def get(self, request, id):
        repo = ProductosRepository()
        producto = repo.get_by_id(id=id)
        try:
            imagen = ProductImage.objects.get(product=producto)
        except:
            imagen = None

        return render(
            request,
            'product/detail.html',
            {
                'product': producto,
                'image': imagen,
            }
        )

class ProductDelete(View):
    def get(self, request, id):
        if request.user.is_staff:
            repo = ProductosRepository()
            producto = repo.get_by_id(id=id)
            repo.delete(producto=producto)
        return redirect('product_list')

class ProductUpdate(View):
    def get(self, request, id):
        if request.user.is_staff:
            productRepo = ProductosRepository()
            categoryRepo = CategoriasRepository()

            producto = productRepo.get_by_id(id)
            categorias = categoryRepo.get_all()

            return render(
                request,
                'product/update.html',
                {
                    'product': producto,
                    'categories': categorias,
                }
            )
        else:
            return redirect('product_list')
    
    def post(self, request, id):
        if request.user.is_staff:
            productRepo = ProductosRepository()
            categoryRepo = CategoriasRepository()
            producto = productRepo.get_by_id(id)
            data = request.POST

            name = data.get('name')
            description = data.get('description')
            price = data.get('price')
            categoryId = data.get('category')
            category = categoryRepo.get_by_id(id=categoryId)
            stock = data.get('stock')

            productRepo.update(
                producto = producto,
                nombre=name,
                precio=price,
                cantidad=stock,
                categoria=category,
                descripcion=description,
            )

            return redirect('product_detail', id)
        else:
            return redirect('product_list')
