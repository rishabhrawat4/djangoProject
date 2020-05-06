from django.db import models

# Create your models here.
class PhotoGallery(models.Model):
    img = models.ImageField(upload_to='pics')
