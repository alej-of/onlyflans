from django.db import models
from uuid import uuid4

# Create your models here.
class Flan(models.Model):
    flan_uuid = models.UUIDField()
    name = models.CharField(max_length=64, default='')
    description = models.TextField(default='')
    image_url = models.URLField(default='')
    slug = models.SlugField(default='')
    is_private = models.BooleanField(default=True)

class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid4, editable=False, unique=True)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()