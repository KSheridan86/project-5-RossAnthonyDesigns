from django.shortcuts import render, redirect
from .forms import UpdateNewsletter


def newsletter(request):
    form = UpdateNewsletter()
    if request.method == 'POST':
        form = UpdateNewsletter(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'users/newsletter.html', context)
