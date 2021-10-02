from django.shortcuts import render,get_object_or_404
from .models import Category,Product
from django.core.paginator import Paginator
from cart.forms import CartAddProductForm

# Create your views here.


def product_list(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(PrdAvailable=True)
    if category_slug:
        category = get_object_or_404(Category,slug=category_slug) 
        products = products.filter(PrdCategory=category)

    paginator=Paginator(products,12)
    page=request.GET.get('page')
    products=paginator.get_page(page)
	
    

		
    context = {
            'category':category,
            'categories':categories,
            'products':products
        }
    
    return render(request,'Product/product_list.html',context)


def product_detail(request,id,slug):
    
    product = get_object_or_404(Product,id=id,slug=slug,PrdAvailable=True)
    cart_product_form = CartAddProductForm()  
    context = {
            'product':product,
            'cart_product_form':cart_product_form
            
        }
    return render(request,'Product/product_detail.html',context)

