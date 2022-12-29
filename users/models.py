from django.db import models
import uuid


class Newsletter(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, blank=False, null=True)
    email = models.EmailField(max_length=500, blank=False, null=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return str(self.email)


class Message(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, blank=False, null=True)
    email = models.EmailField(max_length=500, blank=False, null=True)
    message = models.TextField(max_length=1000, blank=False, null=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return str(f"New message from {self.name}")


class Review(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, blank=False, null=True)
    review = models.TextField(max_length=1000, blank=False, null=True)
    public = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return str(f"New review from {self.name}")
