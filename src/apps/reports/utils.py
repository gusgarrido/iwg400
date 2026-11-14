from typing import Callable, Concatenate, ParamSpec

from django.http import HttpRequest, HttpResponse, HttpResponsePermanentRedirect

P = ParamSpec("P")


def require_login(
    f: Callable[Concatenate[HttpRequest, P], HttpResponse], /
) -> Callable[Concatenate[HttpRequest, P], HttpResponse]:

    def wrapper(req: HttpRequest, *args: P.args, **kwargs: P.kwargs) -> HttpResponse:
        if not req.user.is_authenticated:
            return HttpResponsePermanentRedirect("/accounts")
        return f(req, *args, **kwargs)

    return wrapper
