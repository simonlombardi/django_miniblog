from django import forms

from productos.models import (
    Productos,
    Category,
    Supplier,
    ProductReview,
    ProductImage,
)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = [
            'name',
            'description',
            'price',
            'category',
            'stock',      
            ]
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),  
        }

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = [
            'product',
            'image',
            'description',
        ]