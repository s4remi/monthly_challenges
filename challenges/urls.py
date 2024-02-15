from django.urls import path
from . import views

urlpatterns = [
    # path("february", views.february),
    # path("march", views.march),
    path("<int:month>", views.monthly_number_challenge),
    # adding key name to make sure we are able to have a dynamic url path instead of
    # hard coding it in the views.py
    path("<str:month>", views.monthly_challenge, name="month-challenge"),
]
