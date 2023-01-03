from django.forms import ModelForm
from django import forms
from .models import Newsletter, Message, Review


class UpdateNewsletter(ModelForm):
    class Meta:
        model = Newsletter
        fields = ['name', 'email']

    def __init__(self, *args, **kwargs):
        super(UpdateNewsletter, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Enter your Name...'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Enter your Email...'})


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'message']

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Enter your Name...'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Enter your Email...'})
        self.fields['message'].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Enter your Message...'})


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'review', 'public']

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Enter your Name...'})
        self.fields['review'].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Enter your review...'})
