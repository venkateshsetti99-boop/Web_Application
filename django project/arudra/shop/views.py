from django.shortcuts import render
from django.http import HttpResponse
from .product import Product
from .category import Category

# Create your views here.
def home(request):
    categorys = Category.objects.all()
    categoryID=request.GET.get('cat')
    if categoryID:
        products = Product.get_category_id(categoryID)
    else:
        products = Product.objects.all()
    data = {
        'products': products,
        'categorys': categorys
    }
    return render(request,'index.html',data)