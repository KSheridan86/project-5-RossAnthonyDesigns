from django.shortcuts import render
from .models import Sculpture


def shop(request):
    page = 'shop'
    sculptures = Sculpture.objects.all()
    context = {
        'sculptures': sculptures,
        'page': page
    }
    return render(request, 'sculptures/shop.html', context)
