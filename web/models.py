from django.db import models

# Create your models here.
class Flan(models.Model):
    flan_uuid = models.UUIDField()
    name = models.CharField(max_length=64, default='')
    description = models.TextField(default='')
    image_url = models.URLField(default='')
    slug = models.SlugField(default='')
    is_private = models.BooleanField(default=True)
