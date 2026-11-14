from datetime import datetime
from typing import TYPE_CHECKING

from django.conf import settings
from django.db.models import CASCADE, CharField, DateTimeField, ForeignKey, Model

if TYPE_CHECKING:
    from ..accounts.models import Restaurant


class Report(Model):
    KINDS = [
        ("security", "Seguridad"),
        ("infrastructure", "Infraestructura"),
        ("service", "Servicio"),
        ("accident", "Accidente"),
        ("other", "Otro"),
    ]

    SEVERITIES = [("low", "Baja"), ("medium", "Mediana"), ("high", "Alta"), ("critical", "Crítica")]

    origin: ForeignKey[Restaurant] = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    kind: CharField[str] = CharField(max_length=16, choices=KINDS)
    description: CharField[str] = CharField()
    date: DateTimeField[datetime] = DateTimeField()
    severity: CharField[str] = CharField(max_length=8, choices=SEVERITIES)
    created: DateTimeField[datetime] = DateTimeField(auto_now_add=True)
