from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from sculptures.models import Sculpture


def view_cart(request):
    """View cart function"""
    context = {}
    return render(request, 'cart/cart.html', context)


def add_to_cart(request, item_id):
    """
    Adds product to cart,
    Updates cart with product and product quantity.
    """
    piece = get_object_or_404(Sculpture, id=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    try:
        if item_id in list(cart.keys()):
            if piece.quantity >= cart[item_id] + quantity:
                cart[item_id] += quantity
                messages.success(
                    request, f'{piece} succesfully added to Cart!')
            else:
                messages.error(
                    request,
                    f'Sorry, only {piece.quantity}\
                        of these are curently available.')
        else:
            cart[item_id] = quantity
            messages.success(
                    request, f'{piece} succesfully added to Cart!')
    except RuntimeError:
        messages.error(
            request,
            "Whoops, We've encountered a problem, we'll get straight onto it,\
                in the meantime you could always try again??")

    request.session['cart'] = cart
    return redirect(redirect_url)


def subtract_from_cart(request, item_id):
    """
    Subtracts product to cart,
    Updates cart with product and product quantity.
    """
    piece = get_object_or_404(Sculpture, id=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    try:
        if quantity == 1:
            del cart[item_id]
        elif quantity > 1:
            if item_id in list(cart.keys()):
                cart[item_id] = quantity-1
        else:
            quantity = quantity
    except ValueError:
        messages.error(
            request,
            "Whoops, We've encountered a problem, we'll get straight onto it,\
                in the meantime you could always try again??")

    messages.success(request, f'{piece} succesfully removed from Cart!')
    request.session['cart'] = cart
    return redirect(redirect_url)


def delete_item_from_cart(request, item_id):
    piece = get_object_or_404(Sculpture, id=item_id)
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    try:
        if item_id in list(cart.keys()):
            del cart[item_id]
    except RuntimeError:
        messages.error(request, "Captain, We've got a situation!")

    messages.success(request, f'{piece} succesfully removed from Cart!')
    request.session['cart'] = cart
    return redirect(redirect_url)


def delete_cart(request):
    """Function to delete entire contents of cart"""
    request.session['cart'] = {}
    messages.success(request, 'Cart contents deleted!')
    return redirect('view_cart')
