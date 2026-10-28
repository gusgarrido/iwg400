from django.http import HttpRequest, HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render

from .models import Report, Restaurant


def index(request: HttpRequest) -> HttpResponse:
    ctx: dict[str, object] = {"reports": Report.objects.order_by("-date")}
    return render(request, "index.html", ctx)


def create_report(request: HttpRequest) -> HttpResponse:
    # TODO: vincular reporte con sesión activa
    origin, _ = Restaurant.objects.get_or_create(name="NULL", defaults={"lat": 0, "lon": 0})

    data = request.POST
    r = Report(
        origin=origin, kind=data["kind"], description=data["description"], date=data["date"], severity=data["severity"]
    )
    r.save()
    return HttpResponsePermanentRedirect("/reports")


def generate_stats(request: HttpRequest) -> HttpResponse:
    reports = Report.objects.filter(
        **{
            (kwarg or filt): request.GET[filt]
            for kwarg, filt in {
                (None, "kind"),
                (None, "severity"),
                ("date__date__gte", "before"),
                ("date__date__lte", "after"),
            }
            if filt in request.GET
        }
    )
    ctx: dict[str, object] = {
        "reports": [
            {
                "restaurant": {"name": r.origin.name, "lat": r.origin.lat, "lon": r.origin.lon},
                "kind": r.kind,
                "severity": r.severity,
                "date": r.date.isoformat(),
            }
            for r in reports
        ]
    }
    return render(request, "stats.html", ctx)
