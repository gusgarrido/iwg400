from django.contrib import auth
from django.http import HttpRequest, HttpResponse, HttpResponsePermanentRedirect


def logout_redirect(req: HttpRequest) -> HttpResponse:
    auth.logout(req)
    return HttpResponsePermanentRedirect("/accounts")
