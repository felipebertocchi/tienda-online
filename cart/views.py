from django.shortcuts import render, redirect
from .cart import Cart
from store.models import Product

def cart(request):
    context = {}
    return render(request, 'cart.html', context)

def add_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.add(product=product)

    return redirect('cart:cart')

def substract_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.substract(product=product)

    return redirect('cart:cart')

def remove_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.remove(product=product)

    return redirect('cart:cart')

def clear_cart(request):
    cart = Cart(request)
    cart.clear()

    return redirect('cart:cart')