from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new", views.create_report, name="create_report"),
    path("stats", views.generate_stats, name="generate_stats"),
]
