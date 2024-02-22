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
        if request.method == 'GET' and 'sort_by' in request.GET:
            sort_option = request.GET.get('sort_by')
            if sort_option == '1':  # Change these values according to your options
                # Perform sorting based on relevance
                queryset = Product.objects.order_by('relevance_field')
            elif sort_option == '2':
                # Perform sorting based on name, A to Z
                queryset = Product.objects.order_by('title')
            elif sort_option == '3':
                # Perform sorting based on name, Z to A
                queryset = Product.objects.order_by('-title')
            elif sort_option == '4':
                # Perform sorting based on price, low to high
                queryset = Product.objects.order_by('price')
            elif sort_option == '5':
                # Perform sorting based on price, high to low
                queryset = Product.objects.order_by('-price')
            else:
                # Default sorting option
                queryset = Product.objects.all()
        else:
            queryset = Product.objects.all()

        context = {
            'objects': queryset,
            'product': Product.objects.get(slug=slug)
        }
        return render(request, 'product_detail.html', context)
