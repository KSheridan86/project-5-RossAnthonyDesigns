from django.shortcuts import render, redirect


def view_cart(request):

    context = {

    }
    return render(request, 'cart/cart.html', context)


def add_to_cart(request, item_id):
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def delete_cart(request):
    request.session['cart'] = {}
    return redirect('view_cart')
