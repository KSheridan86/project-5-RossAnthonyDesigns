from django.db import models
import uuid
from cloudinary.models import CloudinaryField


class AddToGallery(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=200, unique=True)
    image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Helper function to organize sculptures by newest first
        """
        ordering = ['-created_on']

    def __str__(self):
        return str(self.title)
