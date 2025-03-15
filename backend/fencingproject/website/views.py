from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response

class sample_api(APIView):
    def get(self, request):
        data = {
            'message': 'Hello, this is a sample API response!'
        }
        return Response(data)


