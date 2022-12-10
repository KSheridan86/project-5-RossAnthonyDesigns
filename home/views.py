from django.shortcuts import render, redirect
from sculptures.models import Sculpture


def index(request):
    page = 'home'
    sculptures = Sculpture.objects.all()[0:3]
    context = {
        'sculptures': sculptures,
        'page': page
    }
    return render(request, 'home/index.html', context)
