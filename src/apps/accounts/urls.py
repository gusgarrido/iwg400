from django.contrib.auth import views as auth_views
from django.http import HttpRequest, HttpResponse, HttpResponsePermanentRedirect
from django.urls import path

from . import views


def index_redirect(req: HttpRequest) -> HttpResponse:
    return HttpResponsePermanentRedirect("/accounts/login")

urlpatterns = [
    path("", index_redirect, name="index"),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", views.logout_redirect, name="logout"),
]
