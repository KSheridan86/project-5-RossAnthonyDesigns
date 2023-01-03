from django.forms import ModelForm
from django import forms
from .models import Sculpture


class AddSculpture(ModelForm):
    class Meta:
        model = Sculpture
        fields = ['title', 'description',
                  'price', 'image', 'quantity', 'available']

    def __init__(self, *args, **kwargs):
        super(AddSculpture, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Add title here...'})
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Please give a short description...'})
        self.fields['price'].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Sculpture Price...'})
        self.fields['image'].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Add Image if Available...'})
        self.fields['quantity'].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Quantity available...'})
        self.fields['available'].widget.attrs.update(
            {'placeholder': 'Available or Not?'})
