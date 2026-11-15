from typing import TYPE_CHECKING

from django.contrib.auth import get_user_model
from django.http import HttpRequest, HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render
from django.views.decorators.http import require_POST

from .models import Report
from .utils import require_login

if TYPE_CHECKING:
    from ..accounts.models import Restaurant as UserModel

Restaurant: type[UserModel] = get_user_model()  # type: ignore


@require_login
def index(request: HttpRequest) -> HttpResponse:
    ctx: dict[str, object] = {"reports": Report.objects.order_by("-date")}
    return render(request, "index.html", ctx)


@require_POST
@require_login
def create_report(request: HttpRequest) -> HttpResponse:
    data = request.POST
    r = Report(
        origin=request.user,
        kind=data["kind"],
        description=data["description"],
        date=data["date"],
        severity=data["severity"],
    )
    r.save()
    return HttpResponsePermanentRedirect("/reports")


@require_login
def generate_stats(request: HttpRequest) -> HttpResponse:
    reports = Report.objects.filter(
        **{
            (kwarg or filt): request.GET[filt]
            for kwarg, filt in {(None, "kind"), (None, "severity"), ("date__gte", "after"), ("date__lte", "before")}
            if filt in request.GET
        }
    )
    ctx: dict[str, object] = {
        "reports": [
            {
                "restaurant": {"name": r.origin.username, "lat": r.origin.lat, "lon": r.origin.lon},
                "kind": r.kind,
                "severity": r.severity,
                "date": r.date.isoformat(),
            }
            for r in reports
        ]
    }
    return render(request, "stats.html", ctx)
