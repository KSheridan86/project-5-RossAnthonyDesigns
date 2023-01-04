from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Sculpture
from .forms import AddSculpture


def shop(request):
    """
    Displays the shop page, and allows sorting by price.
    Page variable is used for the active link in the navbar.
    """
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
    """
    Gets an individual product page or returns a 404 page
    """
    try:
        piece = get_object_or_404(Sculpture, id=pk)
    except RuntimeError:
        messages.error(
            request,
            "Whoops, something has gone wrong, we'll get right on to it")
    context = {
        'piece': piece
    }
    return render(request, 'sculptures/single-item.html', context)


@login_required(login_url='account_login')
def add_sculpture(request):
    """
    Post method adds product to the database
    User needs to be logged in and a superuser.
    Get method displays the add sculpture form.
    """
    form = AddSculpture()
    try:
        if request.method == 'POST' and request.user.is_superuser:
            form = AddSculpture(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Product added successfully!')
                return redirect('dashboard')
    except ValueError:
        messages.error(
            request,
            'Whoops, looks like you might not be authorised\
                to view this page.')
    context = {
        'form': form,
    }
    return render(request, 'sculptures/add_sculpture.html', context)


@login_required(login_url='account_login')
def edit_sculpture(request, pk):
    """
    Post method edits product in the database
    User needs to be logged in and a superuser.
    Get method displays the edit sculpture form.
    """
    piece = get_object_or_404(Sculpture, id=pk)
    form = AddSculpture(instance=piece)
    try:
        if request.method == 'POST' and request.user.is_superuser:
            form = AddSculpture(request.POST, request.FILES, instance=piece)
            if form.is_valid():
                form.save()
                messages.success(request, 'Product edited successfully!')
                return redirect('dashboard')
    except ValueError:
        messages.error(
            request,
            'Whoops, looks like you might not be authorised\
                to perform this action.')
    context = {
        'form': form,
        'piece': piece
    }
    return render(request, 'sculptures/edit_sculpture.html', context)


@login_required(login_url='account_login')
def delete_sculpture(request, pk):
    """
    Post method deletes product from the database
    User needs to be logged in and a superuser.
    Get method displays the delete warning message.
    """
    piece = get_object_or_404(Sculpture, id=pk)
    try:
        if request.method == 'POST' and request.user.is_superuser:
            piece.delete()
            messages.success(request, 'Product deleted successfully!')
            return redirect('dashboard')
    except RuntimeError:
        messages.error(
            request,
            'Whoops, looks like you might not be authorised\
                to perform this action.')
    context = {
        'piece': piece
    }
    return render(request, 'sculptures/delete_sculpture.html', context)
