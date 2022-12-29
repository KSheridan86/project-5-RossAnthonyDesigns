from django.shortcuts import render, redirect
from sculptures.models import Sculpture
from users.models import Review


def index(request):
    page = 'home'
    sculptures = Sculpture.objects.all()[0:3]
    testimonials = {
        'review1': Review.objects.all()[0:1],
        'review2': Review.objects.all()[1:2],
        'review3': Review.objects.all()[2:3],
        'review4': Review.objects.all()[3:4],
        'review5': Review.objects.all()[4:5]
    }

    context = {
        'sculptures': sculptures,
        'page': page,
        'testimonials': testimonials
    }
    return render(request, 'home/index.html', context)


def artist(request):
    page = 'artist'
    context = {
        'page': page,
    }
    return render(request, 'home/artist.html', context)
