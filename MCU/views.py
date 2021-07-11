from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Movie

# Create your views here.

def index(request):
    
    template = loader.get_template('MCU/index.html')
    data = Movie.objects.all()
    mov = {
        'movie_id': data,
    }
    return render(request, 'MCU/index.html', mov)

def series(request):
    return render(request, 'MCU/series.html')

def test(request):
    return HttpResponse('text')