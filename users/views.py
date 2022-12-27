from django.shortcuts import render, redirect
from .forms import UpdateNewsletter


def newsletter(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        redirect_url = request.POST['redirect_url']

        form = UpdateNewsletter(request.POST)
        newsletter = form.save(commit=False)
        newsletter.name = name
        newsletter.email = email
        newsletter.save()

        return redirect(redirect_url)
