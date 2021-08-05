from rest_framework.response import Response
from rest_framework.views import APIView

from rest_fizzbuzz.exceptions import QueryParameterMissing
from rest_fizzbuzz.models import FizzBuzzRequest
from rest_fizzbuzz.utils import my_fizzbuzz


class MyFizzBuzz(APIView):
    def get_query_parameter(self, parameter: str, is_integer: bool = False):
        query_param = self.request.query_params.get(parameter)
        if not query_param:
            raise QueryParameterMissing(parameter)
        if (
            is_integer
        ):  ## TODO deal with is_integer=True but the given value is not an integer
            query_param = int(query_param)
        return query_param

    def get(self, request):
        queryparams = {
            "int1": self.get_query_parameter("int1", is_integer=True),
            "int2": self.get_query_parameter("int2", is_integer=True),
            "limit": self.get_query_parameter("limit", is_integer=True),
            "string1": self.get_query_parameter("string1"),
            "string2": self.get_query_parameter("string2"),
        }

        fizz_buzz_request = FizzBuzzRequest.objects.get_or_create(**queryparams)
        fizz_buzz_request = FizzBuzzRequest.objects.get(**queryparams)
        fizz_buzz_request.count += 1
        fizz_buzz_request.save()

        return Response({"data": my_fizzbuzz(**queryparams)}, 200)


class Statistics(APIView):
    def get(self, request):
        fizz_buzz_request = FizzBuzzRequest.get_most_popular()
        return Response({"data": fizz_buzz_request.int2})
