from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# def february(request):
#     return HttpResponse("this challenge is created for Feb via Ali Sarmei!")


# def march(request):
#     return HttpResponse("this challenge is created for March via  Ali Sarmei.")


def monthly_challenge(request, month):
    challenge_text = None
    if month == "february":
        challenge_text = "Feb Challenge"
    elif month == "march":
        challenge_text = "March Challenge"
    else:
        return HttpResponse("<h1>Invalid Month</h1><p>Please enter a valid month.</p>")
    return HttpResponse(challenge_text)
