from django.shortcuts import render
from django.views import View

from product.models import Product, Category, Size, Color


class ProductView(View):
    def get(self, request):
        context = {
            'product': Product.objects.all(),
            'category': Category.objects.all(),
            'size': Size.objects.all(),
            'color': Color.objects.all(),
        }
        return render(request, 'shop-left-sidebar-col-3.html', context)


class ProductDetailView(View):
    def get(self, request, slug):
        context = {
            'product': Product.objects.get(slug=slug)
        }
        return render(request, 'product_detail.html', context)
