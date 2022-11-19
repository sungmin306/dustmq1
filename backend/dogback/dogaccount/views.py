from django.shortcuts import render
from .models import DogAccount#, DogWeight
from .serializers import Dog_accountSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.http import Http404
#from yolov5 import detect as yolo
# Create your views here.

# 비문추출 값 추가

# #이미지 받는 값
# class Imgviewset(viewsets.ModelViewSet):
#     serializer_class = Nose_vectorSerializer
#     queryset = Nose_vector.objects.all()

# 비문 추출 하는 함수
# @csrf_exempt
# def extraction_vec(request):
#     global dic
#     dic = {'return_value' : '0'}
#     if request.method == 'POST':
#         nose = Nose_vector() # nose라는 변수에 테이블 대입
#         nose.image = request.POST['image']
#         # 이미지 값을 활용해서 벡터추출
#         nose.nose_vec = 1 #임의로 값 저장
#         nose.save()
#         dic['return_value']=1
#         return json(dic)

#     if request.meth0d == 'GET':
#         global data
#         data={}
#         # 이미지 값을 처리 -> 벡터 결과 추출
#         value = 1 # vector
#         dog_data = Dog_account.objects.all()
#         queryset = dog_data.select_vec.filter(nose_vec = value)
#         dic=queryset
#         return json(data)
        
#     if dic['return_val'] == 0:
#         return json(dic)

class DogProfile(APIView):
    def post(self, request): # Create
        serializer = Dog_accountSerializer(data = request.data)
        if serializer.is_valid(): # 유효성 검사
            #이미지 -> 비문 추출 -> 비분추출 값 저장
           # yolo.main(yolo.opt)
            
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class DogDetail(APIView):
    def get_object(self,pk):
        try:
            return DogAccount.objects.get(pk=pk)
        except DogAccount.NotExist:
            raise Http404
    
    def get(self, request, pk, format = None): #Read
        profile = self.get_object(pk)
        serializer = Dog_accountSerializer(profile)
        return Response(serializer.data)

    def put(self, request, pk, format = None): # Update
        profile = self.get_object(pk)
        serializer = Dog_accountSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, requesst, pk, format = None): #Delete
        profile = self.get_object(pk)
        profile.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)



class DogViewSet(viewsets.ModelViewSet): #viewset 활용 CRUD
    serializer_class = Dog_accountSerializer
    queryset = DogAccount.objects.all()
    def perform_create(self, serializer):
        #yolo.main(yolo.opt)
        serializer.save(user = self.request.user)


# #몸무게 체크 및 목록 보내주는 함수
# @csrf_exempt
# def DogWeightView(request):
#     if(request.method == 'POST'):
#         data = json.load(request)
#         Raccount=DogAccount.objects.filter(DogAccount__pet_name = data['petname'])

#         return Response(Raccount.objects.all())
        

        




# class DogProfileViewSet(viewsets.ModelViewSet):
#     serializer_calss = DogWeightSerializer
#     queryset = DogAccount.objects.all()