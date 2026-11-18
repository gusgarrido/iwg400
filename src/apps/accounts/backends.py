from __future__ import annotations

from typing import TYPE_CHECKING

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

from django.http import HttpRequest

if TYPE_CHECKING:
    from .models import Restaurant as RestaurantModel


class EmailAuthBackend(ModelBackend):
    def authenticate(
        self, request: HttpRequest, username: str | None = None, password: str | None = None, **kwargs: object
    ) -> RestaurantModel | None:
        email = kwargs.get("email")
        if password is None:
            return None

        Restaurant = get_user_model()

        try:
            user: RestaurantModel = Restaurant.objects.get(email__iexact=email)  # type: ignore
        except Restaurant.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None
