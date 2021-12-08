from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<h2>kiszki masza grają A mózg na cymbałkach</h2>")

