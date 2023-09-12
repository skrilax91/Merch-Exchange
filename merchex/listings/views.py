from django.shortcuts import render
from .models import Band


def band_index(request):
    bands = Band.objects.all()
    return render(request, 'listings/band/index.html', {'bands': bands})


def band_detail(request, band_id):
    band = Band.objects.get(id=band_id)
    return render(request, 'listings/band/detail.html', {'band': band})
