from django.shortcuts import render
from .models import Diary
from .serializers import DiarySerializers
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.http import Http404


# Create your views here.

class DiaryViewSet(viewsets.ModelViewSet): #viewset 활용 CRUD
    serializer_class = DiarySerializers
    queryset = Diary.objects.all()
