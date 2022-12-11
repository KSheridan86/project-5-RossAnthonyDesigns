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


def single_item(request, pk):
    piece = Sculpture.objects.get(id=pk)

    context = {
        'piece': piece
    }
    return render(request, 'sculptures/single-item.html', context)
