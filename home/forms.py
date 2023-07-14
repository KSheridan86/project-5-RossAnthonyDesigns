from django.forms import ModelForm
from django import forms
from .models import AddToGallery


class GalleryPicForm(ModelForm):
    class Meta:
        model = AddToGallery
        fields = ['title', 'image']

    def __init__(self, *args, **kwargs):
        super(GalleryPicForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control',
                'placeholder': 'Add title here...'})
        self.fields['image'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['image'].help_text = ''
