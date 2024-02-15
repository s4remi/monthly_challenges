from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


# Create your views here.
# def february(request):
#     return HttpResponse("this challenge is created for Feb via Ali Sarmei!")


# def march(request):
#     return HttpResponse("this challenge is created for March via  Ali Sarmei.")

monthly_challenges = {
    "january": "challenge for JAN",
    "february": "challenge for FEB",
    "march": "challenge for MAR",
    "april": "challenge for APR",
    "may": "challenge for MAY",
    "jun": "challenge for JUN",
    "july": "challenge for JULY",
    "august": "challenge for AUG",
    "september": "challenge for SEP",
    "october": "challenge for OCT",
    "november": "challenge for NOV",
    "december": "challenge for DEC",
}


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not a valid month!")


def monthly_number_challenge(request, month):
    # make sure to use the data as list instead of the object
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month - 1]
    # will be: /challenges/<name of the month> as we wanted
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
