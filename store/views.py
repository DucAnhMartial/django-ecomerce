from django.shortcuts import render
from .models import Category, Product
from django.shortcuts import get_object_or_404
# Create your views here.
def store(request):
  
  all_product = Product.objects.all()
  
  context = {'my_products' : all_product}
  
  return render(request,'store/store.html',context)


def categories(request):
  
  all_categories = Category.objects.all()
  
  return {'all_categories':all_categories} 


def product_info(request,slug):
  
  product = get_object_or_404(Product, slug=slug) #truy vấn đối tượng nếu không có trả về 404
  context = {'product': product}

  return render (request, 'store/product-info.html',context )  