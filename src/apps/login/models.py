from django.contrib.auth.models import AbstractUser
from django.db.models import EmailField, FloatField


class Restaurant(AbstractUser):
    email: EmailField[str] = EmailField(unique=True)
    lat: FloatField[float] = FloatField("latitude")
    lon: FloatField[float] = FloatField("longitude")
