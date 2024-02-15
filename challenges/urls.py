from django.urls import path
from . import views

urlpatterns = [
    # path("february", views.february),
    # path("march", views.march),
    path("<month>", views.monthly_challenge),
]
