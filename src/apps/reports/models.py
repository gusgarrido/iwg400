from datetime import datetime

from django.db.models import CASCADE, BigIntegerField, CharField, DateTimeField, ForeignKey, Model, SmallIntegerField


class Restaurant(Model):
    name: CharField[str] = CharField(max_length=256)
    lat: BigIntegerField[int] = BigIntegerField("latitude")
    lon: BigIntegerField[int] = BigIntegerField("longitude")


class Report(Model):
    origin: ForeignKey[Restaurant] = ForeignKey(Restaurant, on_delete=CASCADE)
    kind: SmallIntegerField[int] = SmallIntegerField()
    description: CharField[str] = CharField()
    date: DateTimeField[datetime] = DateTimeField()
    severity: SmallIntegerField[int] = SmallIntegerField()
