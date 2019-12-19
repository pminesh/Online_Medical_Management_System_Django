from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from Medical_Management.models import Product
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    if request.session.has_key('user_email'):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=product,
                     quantity=cd['quantity'],
                     update_quantity=cd['update'])
        return redirect('cart:cart_detail')
    else:
        #return render(request, "User/login.html")
        return redirect('login1')


def cart_remove(request, product_id):
    if request.session.has_key('user_email'):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
        return redirect('cart:cart_detail')
    else:
        return render(request, "User/login.html")

def cart_detail(request):
    if request.session.has_key('user_email'):
        email = request.session['user_email']
        cart = Cart(request)
        for item in cart:
            item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                       'update': True})
        return render(request, "cart/detail.html",{"user_email":email,"cart": cart})
    else:
        return render(request, "User/login.html")