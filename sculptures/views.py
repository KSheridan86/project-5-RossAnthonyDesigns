from django.shortcuts import render
from .models import Sculpture


def shop(request):
    page = 'shop'
    sculptures = Sculpture.objects.all()

    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'title':
                sortkey = 'lower_title'
                sculptures = sculptures.annotate(lower_title=Lower('title'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            sculptures = sculptures.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    context = {
        'sculptures': sculptures,
        'page': page,
        'current_sorting': current_sorting
    }
    return render(request, 'sculptures/shop.html', context)


def single_item(request, pk):
    piece = Sculpture.objects.get(id=pk)

    context = {
        'piece': piece
    }
    return render(request, 'sculptures/single-item.html', context)
