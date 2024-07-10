from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Productos(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField(null = True)
    price = models.DecimalField(max_digits = 12,
                                decimal_places = 2)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
        )
    stock = models.IntegerField(default = 0)

    @admin.display(description = 'Rango de Precios')
    def get_price_range(self):
        if self.price > 90000:
            return 'Alto'
        elif 1600 < self.price < 90000:
            return 'Medio'
        else:
            return 'Bajo' 

    def save(self, *args, **kwargs):
        if self.price > 0:
            super().save()
        else:
            print('error')

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class ProductReview(models.Model):
    product = models.ForeignKey(
        Productos,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
    rating = models.IntegerField()

    def __str__(self):
        return f'Review by {self.author.username} for {self.product.name}'


class PriceHistory(models.Model):
    product = models.ForeignKey(
        Productos, 
        on_delete=models.CASCADE, 
        related_name='price_history'
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.product.name} - {self.price} on {self.date}'


class ProductImage(models.Model):
    product = models.ForeignKey(
        Productos,
        on_delete=models.CASCADE, 
        related_name='images'
    )
    image = models.ImageField(upload_to='product_images/', null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.description or f'Image of {self.product.name}'
