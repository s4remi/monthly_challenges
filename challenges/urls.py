from django.urls import path
from . import views

urlpatterns = [
    # path("february", views.february),
    # path("march", views.march),
    path("<int:month>", views.monthly_number_challenge),
    path("<str:month>", views.monthly_challenge),
]
