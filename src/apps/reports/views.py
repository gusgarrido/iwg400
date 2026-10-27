from django.http import HttpRequest, HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render

from .models import Report, Restaurant


def index(request: HttpRequest) -> HttpResponse:
    ctx: dict[str, object] = {"reports": Report.objects.order_by("date")}
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
    reports = Report.objects.all()
    for kwarg, filt in {
        (None, "kind"),
        (None, "severity"),
        ("date__date__gte", "before"),
        ("date__date__lte", "after"),
    }:
        param = request.GET.get(filt)
        if param:
            reports.filter(**{kwarg or filt: param})
    return HttpResponse("TODO: stuff.")
