from django.shortcuts import render
from .models import Band


def index(request):
    bands = Band.objects.all()
    return render(request, 'listings/index.html', {'bands': bands})
