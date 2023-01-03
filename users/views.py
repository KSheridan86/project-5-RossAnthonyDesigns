from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UpdateNewsletter, MessageForm, ReviewForm
from .models import Newsletter, Message, Review


def newsletter(request):
    try:
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            redirect_url = request.POST['redirect_url']
            already_signed_up = Newsletter.objects.values_list(
                'email', flat=True)

            if email in already_signed_up:
                messages.error(
                    request, "This email address is already signed up!")
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
    except ValueError:
        messages.error(
            request, "Please input your name and a valid Email address....")
        return redirect(redirect_url)


def delete_newsletter(request, pk):
    to_delete = Newsletter.objects.get(id=pk)
    to_delete.delete()
    return redirect('dashboard')


def message(request):
    try:
        if request.method == 'POST':
            redirect_url = request.POST['redirect_url']
            name = request.POST['name']
            email = request.POST['email']
            message = request.POST['message']
            form = MessageForm(request.POST)
            new_message = form.save(commit=False)
            new_message.name = name
            new_message.email = email
            new_message.message = message
            new_message.save()
            messages.success(request, "Message sent!")
        return redirect(redirect_url)
    except ValueError:
        messages.error(
            request, "Please make sure to fill out your Details \
                before leaving a message.")
        return redirect(redirect_url)


@login_required(login_url='/accounts/login/')
def leave_review(request):
    form = ReviewForm()
    try:
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(
                    request, "Review saved, Thank you for your feedback.")
                return redirect('home')
            else:
                messages.error(request, "Please fill in the form...")
    except ValueError:
        messages.error(
            request,
            "Whoops! something has gone wrong, we'll get right on to it.")
    context = {
        'form': form,
    }
    return render(request, 'users/leave_review.html', context)


def view_message(request, pk):
    message = Message.objects.get(id=pk)
    context = {
        'message': message
    }
    return render(request, 'users/message.html', context)


def delete_message(request, pk):
    message = Message.objects.get(id=pk)
    message.delete()
    return redirect('dashboard')


def view_review(request, pk):
    review = Review.objects.get(id=pk)
    form = ReviewForm(instance=review)
    try:
        if request.method == 'POST':
            form = ReviewForm(request.POST, instance=review)
            if form.is_valid():
                form.save()
                messages.success(
                    request, "Review saved.")
                return redirect('dashboard')
            else:
                messages.error(request, "Please fill in the form...")
    except ValueError:
        messages.error(
            request,
            "Whoops! something has gone wrong, we'll get right on to it.")
    context = {
        'review': review,
        'form': form
    }
    return render(request, 'users/review.html', context)


def delete_review(request, pk):
    review = Review.objects.get(id=pk)
    review.delete()
    return redirect('dashboard')


def edit_review(request):
    form = ReviewForm()
    try:
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(
                    request, "Review saved.")
                return redirect('dashboard')
            else:
                messages.error(request, "Please fill in the form...")
    except ValueError:
        messages.error(
            request,
            "Whoops! something has gone wrong, we'll get right on to it.")
    context = {
        'form': form,
    }
    return render(request, 'users/review.html', context)
