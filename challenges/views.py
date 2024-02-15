from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def february(request):
    return HttpResponse("this challenge is created for Feb via Ali Sarmei!")


def march(request):
    return HttpResponse("this challenge is created for March via  Ali Sarmei.")
