from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, 'Your Cart is Empty!')
        return redirect(reverse('shop'))

    order_form = OrderForm()
    context = {
        'form': order_form,
    }
    return render(request, 'checkout/checkout.html', context)
