from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# from django.template.loader import render_to_string


# Create your views here.

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


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>'
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge(request, month):
    try:
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
        return render(request, "challenges/challenge.html")
    except:
        return HttpResponseNotFound("<h1>This month is not a valid month!</h1>")


def monthly_number_challenge(request, month):
    # make sure to use the data as list instead of the object
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month - 1]
    # will be: /challenges/<name of the month> as we wanted
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
