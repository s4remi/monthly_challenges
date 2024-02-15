from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),  # to saee the list of the month in /challenges
    path("<int:month>", views.monthly_number_challenge),
    # adding key name to make sure we are able to have a dynamic url path instead of
    # hard coding it in the views.py
    path("<str:month>", views.monthly_challenge, name="month-challenge"),
]
