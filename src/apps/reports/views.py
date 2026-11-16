from typing import TYPE_CHECKING

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponsePermanentRedirect, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST

from .models import Report

if TYPE_CHECKING:
    from ..accounts.models import Restaurant as UserModel

Restaurant: type[UserModel] = get_user_model()  # type: ignore


@require_GET
@login_required
def index(request: HttpRequest) -> HttpResponse:
    ctx: dict[str, object] = {"reports": Report.objects.order_by("-date")}
    return render(request, "index.html", ctx)


@require_POST
@login_required
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


@require_GET
@login_required
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
                "restaurant": {"name": r.origin.display_name, "lat": r.origin.lat, "lon": r.origin.lon},
                "kind": r.kind,
                "severity": r.severity,
                "date": r.date.isoformat(),
            }
            for r in reports
        ]
    }
    return render(request, "stats.html", ctx)


@require_GET
def check_alerts(request: HttpRequest) -> JsonResponse:
    last_id = request.GET.get("last_id")

    if last_id is None:
        latest = Report.objects.order_by("-id").first()
        return JsonResponse({"last_id": latest.id if latest else 0, "reports": []})

    try:
        last_id = int(last_id)
        if last_id < 0:
            raise ValueError
    except ValueError:
        return JsonResponse({"error": "ID inválido"}, status=400)

    new_reports = Report.objects.filter(id__gt=last_id).select_related("origin").order_by("id")[:50]
    reports = [
        {
            "id": report.id,
            "kind": report.get_kind_display(),
            "severity": report.get_severity_display(),
            "description": report.description,
        }
        for report in new_reports
    ]

    if reports:
        last_id = reports[-1]["id"]
    return JsonResponse({"last_id": last_id, "reports": reports})
