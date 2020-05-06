from django.shortcuts import render
from .models import PhotoGallery
# Create your views here.

def index(request):

    photos = PhotoGallery.objects.all()
    photos1 = photos[:len(photos) // 2]
    photos2 = photos[len(photos) // 2:]
    return render(request, "index.html", {'photos1': photos1, 'photos2': photos2})
