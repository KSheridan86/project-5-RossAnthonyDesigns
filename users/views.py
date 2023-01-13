from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UpdateNewsletter, MessageForm, ReviewForm
from .models import Newsletter, Message, Review


def newsletter(request):
    """
    Allows user to sign up for a newsletter,
    Checks if the email is already in the database,
    Aborts process and informs user if so.
    """
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


@login_required(login_url='account_login')
def delete_newsletter(request, pk):
    """
    Delete name & email from newsletter,
    Need to be logged in and a superuser to perform this action.
    """
    try:
        if request.user.is_superuser:
            to_delete = get_object_or_404(Newsletter, id=pk)
            to_delete.delete()
            return redirect('dashboard')
        else:
            messages.error(request, 'Maybe try logging in first?')
            return redirect('account_login')
    except RuntimeError:
        messages.error(
            request,
            "Whoops, looks like you're not permitted to perform this action")


def message(request):
    """
    Allows user to send a private message to the site admin.
    """
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


@login_required(login_url='account_login')
def leave_review(request):
    """
    User can submit a product review,
    They must be logged in to do so.
    """
    form = ReviewForm()
    try:
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                update = form.save(commit=False)
                update.email = request.user.email
                update.save()
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


@login_required(login_url='account_login')
def view_message(request, pk):
    """
    Admin can view recieved private messages,
    login & superuser required.
    """
    try:
        if request.user.is_superuser:
            message = get_object_or_404(Message, id=pk)
        else:
            return redirect('home')
    except ValueError:
        messages.error(
            request, "Whoops, looks like you're not authorised to be here!")
    context = {
        'message': message
    }
    return render(request, 'users/message.html', context)


@login_required(login_url='account_login')
def delete_message(request, pk):
    """
    Admin can delete private messages,
    login & superuser required.
    """
    try:
        if request.user.is_superuser:
            message = get_object_or_404(Message, id=pk)
            message.delete()
            return redirect('dashboard')
        else:
            return redirect('home')
    except RuntimeError:
        messages.error(
            request, "Whoops, looks like you're not authorised to be here!")


@login_required(login_url='account_login')
def view_review(request, pk):
    """
    Admin can see and update visibility of customer reviews.
    """
    review = get_object_or_404(Review, id=pk)
    form = ReviewForm(instance=review)
    try:
        if request.method == 'POST' and request.user.is_superuser:
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


@login_required(login_url='account_login')
def delete_review(request, pk):
    """
    Admin can delete customer reviews,
    Required to be logged in and a superuser.
    """
    try:
        if request.user.is_superuser:
            review = get_object_or_404(Review, id=pk)
            review.delete()
            return redirect('dashboard')
    except RuntimeError:
        messages.error(
            request, "Whoops, looks like you're not authorised to be here!")
