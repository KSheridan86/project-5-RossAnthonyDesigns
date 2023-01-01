from django.shortcuts import render, redirect
from sculptures.models import Sculpture
from users.models import Review


def index(request):
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

    while div_number_to_pass_down < vetted_testimonials.__len__() and div_number_to_pass_down < review_limit_of_5:
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
    page = 'artist'
    context = {
        'page': page,
    }
    return render(request, 'home/artist.html', context)
