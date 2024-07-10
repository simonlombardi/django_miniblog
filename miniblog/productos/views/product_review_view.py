from django.views import View
from django.shortcuts import render, redirect

from productos.repositories.reviewRepository import ReviewRepository
from productos.repositories.productosRepository import ProductosRepository

class ProductReviewView(View):
    def get(self, request):
        repo = ReviewRepository()
        reviews = repo.get_all()

        return render(
            request,
            'product_review/list.html',
            {'reviews': reviews}
        )
    
class ProductReviewCreate(View):
    def get(self, request):
        repo = ProductosRepository()
        products = repo.get_all()
        return render(
            request,
            'product_review/create.html',
            {'products': products},
        )
    
    def post(self, request):
        repo = ReviewRepository()
        id_producto = request.POST.get('id_producto')
        opinion = request.POST.get('opinion')
        rating =  request.POST.get('rating')
        user = request.user
        repo.create(id_producto, user, opinion, rating)
        return redirect('review_list')

class ProductReviewDetail(View):
    def get(self, request, id):
        repo = ReviewRepository()
        review = repo.get_by_id(id=id)
        return render(
            request,
            'product_review/detail.html',
            {'review': review},
        )

class ProductReviewUpdate(View):
    def get(self, request, id):
        if request.user.is_authenticated:
            repo = ReviewRepository()
            review = repo.get_by_id(id=id)
            return render(
                request,
                'product_review/update.html',
                {'review': review},
            )
        else:
            return redirect('review_list')

    def post(self, request, id):
        if request.user.is_authenticated:
            repo = ReviewRepository()
            review = repo.get_by_id(id)
            opinion = request.POST.get('opinion')
            rating =  request.POST.get('rating')
            review.text = opinion
            review.rating = rating
            review.save()
        return redirect('review_list')

class ProductReviewDelete(View):
    def get(self, request, id):
        if request.user.is_authenticated:
            repo = ReviewRepository()
            review = repo.get_by_id(id=id)
            repo.delete(review=review)
        return redirect('review_list')
