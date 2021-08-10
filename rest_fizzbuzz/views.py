from rest_framework.response import Response
from rest_framework.views import APIView

from rest_fizzbuzz.exceptions import InvalidQueryParameterValue, QueryParameterMissing
from rest_fizzbuzz.models import FizzBuzzRequest
from rest_fizzbuzz.utils import my_fizzbuzz


class MyFizzBuzz(APIView):
    def get_query_parameter(self, parameter: str, is_integer: bool = False):
        query_param = self.request.query_params.get(parameter)
        if not query_param:
            raise QueryParameterMissing(parameter)
        if is_integer:
            try:
                return int(query_param)
            except ValueError:
                raise InvalidQueryParameterValue(parameter, query_param)
        return query_param

    def get(self, request):
        queryparams = {
            "int1": self.get_query_parameter("int1", is_integer=True),
            "int2": self.get_query_parameter("int2", is_integer=True),
            "limit": self.get_query_parameter("limit", is_integer=True),
            "string1": self.get_query_parameter("string1"),
            "string2": self.get_query_parameter("string2"),
        }

        fizz_buzz_request = FizzBuzzRequest.objects.get_or_create(**queryparams)[0]
        fizz_buzz_request.count += 1
        fizz_buzz_request.save()

        return Response({"data": my_fizzbuzz(**queryparams)}, 200)


class Statistics(APIView):
    def get(self, request):
        fizz_buzz_request = FizzBuzzRequest.get_most_popular()

        if not fizz_buzz_request:
            return Response(
                {
                    "data": {
                        "message": "no request statistics available yet",
                    }
                },
                200,
            )
        return Response(
            {
                "data": {
                    "count": fizz_buzz_request.count,
                    "parameters": {
                        "int1": fizz_buzz_request.int1,
                        "int2": fizz_buzz_request.int2,
                        "limit": fizz_buzz_request.limit,
                        "string1": fizz_buzz_request.string1,
                        "string2": fizz_buzz_request.string2,
                    },
                }
            },
            200,
        )
