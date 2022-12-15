from django.shortcuts import render, redirect
from django.contrib import messages
from sculptures.models import Sculpture


def view_cart(request):
    context = {}
    return render(request, 'cart/cart.html', context)


def add_to_cart(request, item_id):
    piece = Sculpture.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    messages.success(request, f'{piece} succesfully added to Cart!')
    request.session['cart'] = cart
    return redirect(redirect_url)


def subtract_from_cart(request, item_id):
    piece = Sculpture.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if quantity == 1:
        del cart[item_id]
    elif quantity > 1:
        if item_id in list(cart.keys()):
            cart[item_id] = quantity-1
    else:
        quantity = quantity

    messages.success(request, f'{piece} succesfully removed from Cart!')
    request.session['cart'] = cart
    return redirect(redirect_url)


def delete_item_from_cart(request, item_id):
    piece = Sculpture.objects.get(pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        del cart[item_id]

    messages.success(request, f'{piece} succesfully removed from Cart!')
    request.session['cart'] = cart
    return redirect(redirect_url)


def delete_cart(request):
    request.session['cart'] = {}
    messages.success(request, 'Cart contents deleted!')
    return redirect('view_cart')
