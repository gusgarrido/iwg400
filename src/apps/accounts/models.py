from django.contrib.auth.models import AbstractUser
from django.db.models import EmailField, FloatField


class Restaurant(AbstractUser):
    email: EmailField[str] = EmailField(unique=True)
    lat: FloatField[float] = FloatField("latitude", default=0)
    lon: FloatField[float] = FloatField("longitude", default=0)

    @property
    def display_name(self) -> str:
        if self.first_name:
            if self.last_name:
                return f"{self.first_name} {self.last_name}"
            return self.first_name
        return self.username