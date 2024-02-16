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
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {"data": months})


def monthly_challenge(request, month):
    try:
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
        challenge_text = monthly_challenges[month]
        return render(
            request,
            "challenges/challenge.html",
            {
                "text": challenge_text,
                # "title": "Ali Saremi",
                # it is a best practice to leave all html modification in the html file &using tags
                "month_name": month,
            },
        )
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
