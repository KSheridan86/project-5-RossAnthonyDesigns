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
        'stripe_public_key': 'pk_test_51MGPnmACvCGI7S3SEDxEraL67ByQ24nRKFOB08btz8bll9ZC6fcjRrUkeqdMknkinkokLNIf06uQnvVf9hfZ4U0c00OzHdp57Z',
        'client_secret': '123456',
    }
    return render(request, 'checkout/checkout.html', context)
