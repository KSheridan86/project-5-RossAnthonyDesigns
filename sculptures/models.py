from django.db import models
import uuid
from cloudinary.models import CloudinaryField


class Sculpture(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    detailed_description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = CloudinaryField('image', default='placeholder')
    available = models.BooleanField(default=False)
    quantity = models.DecimalField(max_digits=3, decimal_places=0, default="Add Quantity Here...")
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Helper function to organize sculptures by newest first
        """
        ordering = ['-created_on']

    def __str__(self):
        return str(self.title)
