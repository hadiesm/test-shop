from django.shortcuts import render,get_object_or_404
from .models import Category,Product
from cart.forms import AddProductToCartForm
from .recommender import Recommender
# Create your views here.

def main_page(request):
    category = Category.objects.all()
    product_list = Product.objects.filter(available=True)
    recent = Product.objects.all().order_by('-created')
    cart_add_form = AddProductToCartForm()
    context = {'category':category,'product_list':product_list,
               'recent':recent,'cart_add_form':cart_add_form}
    return render(request,'myshop/index.html',context)




def product_list_page(request,category_slug=None):
    categories = Category.objects.all()
    category = None
    products = Product.objects.filter(available=True)
    product_list = Product.objects.filter(available=True)
    cart_add_form = AddProductToCartForm()
    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        product_list = product_list.filter(category = category)
    context = {'categories':categories,'product_list':product_list,'products':products,
               'cart_add_form':cart_add_form}
    return render(request,'myshop/product-list.html',context)

def product_detail_page(request,product_slug):
    category = Category.objects.all()
    product = get_object_or_404(Product,slug=product_slug,available=True)
    product_list = Product.objects.all().filter(available=True)
    cart_add_form = AddProductToCartForm()
    r = Recommender()
    recommended = r.suggest_products([product],5)
    context = {'product':product,'category':category,'cart_add_form':cart_add_form,
               'product_list':product_list,'recommended':recommended}
    return render(request,'myshop/product-detail.html',context)

def contact_page(request):
    return render(request,'myshop/contact.html')

def about_page(request):
    return render(request,'myshop/about.html')

def privacy_page(request):
    return render(request,'myshop/privacy.html')

def terms_page(request):
    return render(request,'myshop/terms.html')

def payment_policy_page(request):
    return render(request,'myshop/payment_policy.html')

def shipping_policy_page(request):
    return render(request,'myshop/shipping_policy.html')

def return_policy_page(request):
    return render(request,'myshop/return_policy.html')

def my_account_page(request):
    return render(request,'myshop/my_account.html')