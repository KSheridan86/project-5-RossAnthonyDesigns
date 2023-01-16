from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from .forms import OrderForm
from cart.contexts import cart_contents
from sculptures.models import Sculpture
from .models import OrderLineItem, Order
import stripe


# add try except block/ask chris about this one
def checkout(request):
    """
    Checkout function, creates users order and calls stripe payments,
    Sends details through to the checkout_success view.
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    try:
        if request.method == 'POST':
            cart = request.session.get('cart', {})
            form_data = {
                'full_name': request.POST['full_name'],
                'email': request.POST['email'],
                'phone_number': request.POST['phone_number'],
                'country': 'Ireland',
                'postcode': request.POST['postcode'],
                'town_or_city': request.POST['town_or_city'],
                'street_address1': request.POST['street_address1'],
                'street_address2': request.POST['street_address2'],
                'county': request.POST['county'],
            }
            order_form = OrderForm(form_data)
            if order_form.is_valid():
                order = order_form.save()
                for item_id, quantity in cart.items():
                    try:
                        product = get_object_or_404(Sculpture, id=item_id)
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=quantity
                        )
                        order_line_item.save()
                    except Sculpture.DoesNotExist:
                        messages.error(request, (
                            'Something has gone wrong with your cart'
                            'Please call us for assistance')
                        )
                        order.delete()
                        return redirect(reverse('view_cart'))
                return redirect(
                    reverse('checkout_success', args=[order.order_number]))
            else:
                messages.error(
                    request,
                    'Something has gone wrong with your order,\
                        Double check your details.')
    except ValueError:
        message.error(request, 'Wait!')

    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, 'Your Cart is Empty!')
            return redirect(reverse('shop'))

        current_cart = cart_contents(request)
        total = current_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing!')

    context = {
        'form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, 'checkout/checkout.html', context)


def checkout_success(request, order_number):
    """
    Calls the order confirmation page,
    Updates stock quantity after successful purchase.
    """
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
                                A confirmation email will been sent to \
                                {order.email}.')

    cart = request.session.get('cart', {})
    alter_quantity = []
    product_object = []
    number = 0
    email_content = f"Hi {order.full_name},\n\nThank you for your order of: \n"

    try:
        for item_id, quantity in cart.items():
            product_object.append(Sculpture.objects.get(id=item_id))
            alter_quantity.append(quantity)

            for item in product_object:
                email_str = (
                    "" + str(item.title) + ", "
                    + "Quantity :" + f"{quantity} \n"
                    + f"\n"
                    + f"We will do our best to ship your items "
                    + f"as soon as possible."
                    + f"\n"
                    + f"If you have any questions about your order "
                    + f"please feel free to get in touch. \n"
                    + f"\n"
                    + f"Kind Regards, \n"
                    + f"The forged Nature Team")
            email_content = email_content + email_str

        send_mail(
            "Thank you for you order!",
            f"{email_content}",
            settings.EMAIL_HOST_USER,
            [order.email],
            fail_silently=False,)

        for item in product_object:
            item.quantity = item.quantity - alter_quantity[number]
            item.save()
            number += 1
    except ValueError:
        messages.error(
            request, "Whoops, we've had a problem reaching our database.")

    del request.session['cart']
    context = {
        'order': order,
    }
    return render(request, 'checkout/checkout_success.html', context)
