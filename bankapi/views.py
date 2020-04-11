from django.shortcuts import render
from rest_framework.views import APIView
from .models import Branch
from django.http import HttpResponse
from django.http import JsonResponse
import requests
from django.core.serializers import  serialize
from .serialzers import BranchSerialzer, BankcitySerialzer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
def index(request):
    return render(request, 'index.html')

class IndexView(APIView):

    def get(self, request, ifsc):
        try:
            branch = Branch.objects.get(ifsc= ifsc)
            serializer = BranchSerialzer(branch)
            return Response (data =serializer.data, status = status.HTTP_200_OK)
        except Exception as e:
            return Response(data="Query data not found", status=status.HTTP_404_NOT_FOUND)


class BranchView(APIView):

    def get(self, request,bank, city):
        try:
            branch = Branch.objects.get(bank=bank,city=city)
            serializer = BankcitySerialzer(branch)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data="Query data not found", status=status.HTTP_404_NOT_FOUND)

