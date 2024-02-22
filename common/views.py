from django.shortcuts import render
from django.views.generic import TemplateView

from product.models import Product


# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'


def search(request):
    search = request.Post.get('search')
    if search:
        product = Product.objects.filter(name__contains=search)

    context = {
        'product': product
    }
    return render(request, 'shop-left-sidebar-col-3.html', )
