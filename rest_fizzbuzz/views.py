from django.http import HttpResponse
from rest_framework.views import APIView


class MyFizzBuzz(APIView):
    def get(self, request):
        int1 = self.request.query_params.get('int1')
        int2 = self.request.query_params.get('int2')
        limit = self.request.query_params.get('limit')
        string1 = self.request.query_params.get('string1')
        string2 = self.request.query_params.get('string2')


        return HttpResponse(f'int1: {int1}, int2: {int2}, limit: {limit}, string1: {string1}, string2: {string2}')
