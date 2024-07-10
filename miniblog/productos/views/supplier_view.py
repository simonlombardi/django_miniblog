from django.views import View
from django.shortcuts import render, redirect

from productos.repositories.supplierRepository import SupplierRepository

repo = SupplierRepository

class SupplierView(View):
    def get(self, request):
        if request.user.is_staff:
            repo = SupplierRepository()
            proveedores = repo.get_all()
            return render(
                request,
                'supplier/list.html',
                {
                    'suppliers': proveedores
                },
            )
        else:
            return redirect('/')
    
class SupplierCreate(View):
    def get(self, request):
        if request.user.is_staff:
            return render(
                request,
                'supplier/create.html'
            )
        else:
            return redirect('/')
    
    def post(self, request):
        if request.user.is_staff:
            repo = SupplierRepository()
            data = request.POST

            name = data.get('name')
            address = data.get('address')
            phone =  data.get('phone')

            newSupplier = repo.create(nombre = name,
                                    direccion = address,
                                    telefono = phone)

            return redirect('supplier_detail', newSupplier.id)
        else:
            return redirect('/')

class SupplierDetail(View):
    def get(self, request, id):
        if request.user.is_staff:
            repo = SupplierRepository()
            proveedor = repo.get_by_id(id)

            return render(
                request,
                'supplier/detail.html',
                {
                    'supplier': proveedor,
                }
            )
        else:
            return redirect('/')

class SupplierDelete(View):
    def get(self, request, id):
        if request.user.is_staff:
            repo = SupplierRepository()
            proveedor = repo.get_by_id(id=id)
            repo.delete(proveedor)
            return redirect('supplier_list')
        else:
            return redirect('/')
    
class SupplierUpdate(View):
    def get(self, request, id):
        if request.user.is_staff:
            repo = SupplierRepository()
            proveedor = repo.get_by_id(id)

            return render(
                request,
                'supplier/update.html',
                {
                    'supplier': proveedor,
                }
            )
        else:
            return redirect('/')
    
    def post(self, request, id):
        if request.user.is_staff:
            repo = SupplierRepository()
            proveedor = repo.get_by_id(id)

            data = request.POST
            name = data.get('name')
            address = data.get('address')
            phone =  data.get('phone')

            repo.update(proveedor = proveedor,
                        nombre = name,
                        direccion = address,
                        telefono = phone)

            return redirect('supplier_detail', id)
        else:
            return redirect('/')
