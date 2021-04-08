from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_POST
from myshop.models import Product
from .cart import Cart
from .forms import AddProductToCartForm
# Create your views here.

@require_POST
def card_add(request,product_id):
    cart = Cart(request)
    product = get_object_or_404(Product,id=product_id)
    form = AddProductToCartForm(request.POST)
    if form.is_valid():
        cdata = form.cleaned_data
        cart.add(product=product,quantity=cdata['quantity'],
                 override_quantity=cdata['override'])
    return redirect('cart:cart_detail')

@require_POST
def cart_remove(request,product_id):
    cart = Cart(request)
    product = get_object_or_404(Product,id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = AddProductToCartForm(initial={
            'quantity':item['quantity'],'override':True
        })
    context = {'cart':cart}
    return render(request,'cart/cart_detail.html',context)