from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import APIException


class QueryParameterMissing(APIException):
    status_code = 400
    default_detail = "Mandatory query parameter missing"

    def __init__(self, parameter: str, **kwargs):
        detail = _(f'{self.default_detail}: "{parameter}"')
        super().__init__(detail=detail, **kwargs)


class InvalidQueryParameterValue(APIException):
    status_code = 400
    default_detail = "Invalid query parameter value"

    def __init__(self, parameter: str, value: str, **kwargs):
        detail = _(
            f'{self.default_detail}: "{value}" is an invalid value for "{parameter}"'
        )
        super().__init__(detail=detail, **kwargs)
