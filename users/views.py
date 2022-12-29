from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UpdateNewsletter
from .models import Newsletter


# possibly limit sign up to once per user/check if email is in database
def newsletter(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        redirect_url = request.POST['redirect_url']
        already_signed_up = Newsletter.objects.values_list('email', flat=True)

        if email in already_signed_up:
            messages.error(request, "This email address is already signed up!")
        else:
            form = UpdateNewsletter(request.POST)
            newsletter = form.save(commit=False)
            newsletter.name = name
            newsletter.email = email
            newsletter.save()
            messages.success(
                request,
                f"{email} has been successfully added to our mailing list")
        return redirect(redirect_url)
