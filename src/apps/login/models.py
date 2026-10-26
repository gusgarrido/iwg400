from datetime import datetime

from django.db.models import CharField, DateTimeField, Model


class User(Model):
    username: CharField[str] = CharField(max_length=256)
    email: CharField[str] = CharField(max_length=256)
    ps: CharField[str] = CharField("password hash", max_length=256)
    created: DateTimeField[datetime] = DateTimeField("creation date")
