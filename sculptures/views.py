from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Sculpture
from .forms import AddSculpture


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


@login_required(login_url='/accounts/login/')
def add_sculpture(request):
    form = AddSculpture()
    if request.method == 'POST':
        form = AddSculpture(request.POST, request.FILES)
        if form.is_valid():
            new_sculpture = form.save(commit=False)
            new_sculpture.save()
            return redirect('shop')
    context = {
        'form': form,
    }
    return render(request, 'sculptures/add_sculpture.html', context)


@login_required(login_url='/accounts/login/')
def edit_sculpture(request, pk):
    piece = Sculpture.objects.get(id=pk)
    form = AddSculpture(instance=piece)
    if request.method == 'POST':
        form = AddSculpture(request.POST, request.FILES, instance=piece)
        if form.is_valid():
            new_sculpture = form.save(commit=False)
            new_sculpture.save()
            return redirect('shop')
    context = {
        'form': form,
        'piece': piece
    }
    return render(request, 'sculptures/edit_sculpture.html', context)


@login_required(login_url='/accounts/login/')
def delete_sculpture(request, pk):
    piece = Sculpture.objects.get(id=pk)
    if request.method == 'POST':
        piece.delete()
        return redirect('shop')
    context = {
        'piece': piece
    }
    return render(request, 'sculptures/delete_sculpture.html', context)
