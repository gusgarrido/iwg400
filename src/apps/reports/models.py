from datetime import datetime

from django.db.models import CASCADE, BigIntegerField, CharField, DateTimeField, ForeignKey, Model


class Restaurant(Model):
    name: CharField[str] = CharField(max_length=256)
    lat: BigIntegerField[int] = BigIntegerField("latitude")
    lon: BigIntegerField[int] = BigIntegerField("longitude")


class Report(Model):
    KINDS = [
        ("security", "Seguridad"),
        ("infrastructure", "Infraestructura"),
        ("service", "Servicio"),
        ("accident", "Accidente"),
        ("other", "Otro"),
    ]

    SEVERITIES = [("low", "Baja"), ("medium", "Mediana"), ("high", "Alta"), ("critical", "Crítica")]

    origin: ForeignKey[Restaurant] = ForeignKey(Restaurant, on_delete=CASCADE)
    kind: CharField[str] = CharField(max_length=16, choices=KINDS)
    description: CharField[str] = CharField()
    date: DateTimeField[datetime] = DateTimeField()
    severity: CharField[str] = CharField(max_length=8, choices=SEVERITIES)
    created: DateTimeField[datetime] = DateTimeField(auto_now_add=True)
