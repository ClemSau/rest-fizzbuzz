from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import APIException


class QueryParameterMissing(APIException):
    status_code = 400
    default_detail = "Mandatory query parameter missing"

    def __init__(self, parameter: str, **kwargs):
        detail = _(f"{self.default_detail}: {parameter}")
        super().__init__(detail=detail, **kwargs)
