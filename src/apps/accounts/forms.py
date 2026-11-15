from typing import TYPE_CHECKING

from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm

from .models import Restaurant

if TYPE_CHECKING:
    AuthFormBase = AuthenticationForm[Restaurant]
else:
    AuthFormBase = AuthenticationForm


class EmailAuthenticationForm(AuthFormBase):
    def clean(self) -> dict[str, object]:
        email = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if email is not None and password:
            self.user_cache = authenticate(self.request, email=email, password=password)  # type: ignore
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data
