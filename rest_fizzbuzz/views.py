from rest_framework.response import Response
from rest_framework.views import APIView

from rest_fizzbuzz.utils import my_fizzbuzz

from rest_fizzbuzz.exceptions import QueryParameterMissing


class MyFizzBuzz(APIView):
    def get_query_parameter(self, parameter: str, is_integer: bool = False):
        query_param = self.request.query_params.get(parameter)
        if not query_param:
            raise QueryParameterMissing(parameter)
        if is_integer:
            query_param = int(query_param)
        return query_param

    def get(self, request):
        int1 = self.get_query_parameter("int1", is_integer=True)
        int2 = self.get_query_parameter("int2", is_integer=True)
        limit = self.get_query_parameter("limit", is_integer=True)
        string1 = self.get_query_parameter("string1")
        string2 = self.get_query_parameter("string2")

        return Response({"data": my_fizzbuzz(int1, int2, limit, string1, string2)}, 200)
