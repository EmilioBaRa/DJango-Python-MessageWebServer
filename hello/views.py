from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def myFirstDjangoWP(request):
    return HttpResponse("Hello world!")
