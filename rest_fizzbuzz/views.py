from django.http import HttpResponse
from rest_framework.views import APIView

from rest_fizzbuzz.utils import my_fizzbuzz


class MyFizzBuzz(APIView):
    def get(self, request):
        int1 = int(self.request.query_params.get("int1"))
        int2 = int(self.request.query_params.get("int2"))
        limit = int(self.request.query_params.get("limit"))
        string1 = self.request.query_params.get("string1")
        string2 = self.request.query_params.get("string2")

        return HttpResponse(my_fizzbuzz(int1, int2, limit, string1, string2))
