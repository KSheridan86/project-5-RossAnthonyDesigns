from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from sculptures.models import Sculpture
from users.models import Newsletter, Message, Review
from users.models import Review
from checkout.models import Order


def index(request):
    """
    Displays the home page with featured sculptures,
    Sorts testimonials by public visibility,
    Page variable is used for the active link in the navbar.
    """
    page = 'home'
    sculptures = Sculpture.objects.all()[0:3]
    all_testimonials = Review.objects.all()
    vetted_testimonials = []
    numbered_testimonial_divs = ['One', 'Two', 'Three', 'Four', 'Five']
    div_number_to_pass_down = 0
    review_limit_of_5 = 5

    for review in all_testimonials:
        if review.public is True:
            vetted_testimonials.append(review)

    while div_number_to_pass_down < vetted_testimonials.__len__(
                ) and div_number_to_pass_down < review_limit_of_5:
        vetted_testimonials[
            div_number_to_pass_down
            ].number = numbered_testimonial_divs[div_number_to_pass_down]
        div_number_to_pass_down = div_number_to_pass_down + 1

    context = {
        'sculptures': sculptures,
        'page': page,
        'vetted_testimonials': vetted_testimonials[0:5]
    }
    return render(request, 'home/index.html', context)


def artist(request):
    """
    Displays the artist page,
    Page variable is used for the active link in the navbar.
    """
    page = 'artist'
    context = {
        'page': page,
    }
    return render(request, 'home/artist.html', context)


@login_required(login_url='account_login')
def dashboard(request):
    """
    User needs to be logged in and a superuser.
    If so the admin dashboard page is loaded,
    All site Crud functionality is available here.
    """
    page = 'dashboard'
    try:
        if request.user.is_superuser:
            sculptures = Sculpture.objects.all()
            reviews = Review.objects.all()
            newsletter = Newsletter.objects.all()
            message = Message.objects.all()
            orders = Order.objects.all()
        else:
            return redirect('account_login')
    except RuntimeError:
        messages.error(
            request,
            'Whoops, looks like you might not be authorised\
                to access this page.')
    context = {
        'reviews': reviews,
        'sculptures': sculptures,
        'newsletter': newsletter,
        'message': message,
        'orders': orders,
        'page': page
    }
    return render(request, 'home/dashboard.html', context)
