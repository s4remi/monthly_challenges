from django.urls import path
from . import views

urlpatterns = [path("february", views.index)]
