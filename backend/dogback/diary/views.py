from django.shortcuts import render
from .models import Diary#, PetWalk
from .serializers import DiarySerializers
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.http import Http404
import json
from django.http import JsonResponse
from django.db.models import Q

# Create your views here.

class DiaryViewSet(viewsets.ModelViewSet): #viewset 활용 CRUD
    serializer_class = DiarySerializers
    queryset = Diary.objects.all()

    def create(self, request):
        # serializer.save(user=self.request.user)
        print(self.request.user) # admin 만 나온다.
        #print("Diary.user 출력")
        #print(Diary.user)
        serializer = self.get_serializer(data=request.data) # serializer 은 serializer_class를 의미(?)
        #petwalklist = Diary.objects.filter(Q(user__username = self.request.user) & Q(petwalk__exact = 'o'))# username 과 username이 같은 값 모두 UserPetLis ->clear
        # print("serializer 출력합니다")
        # print(serializer)
        # print("petwalklist 출력합니다.")
        # print(petwalklist)
        #w_num = len(petwalklist)
        #print(w_num)#->clear
        if serializer.is_valid():
            #print(petwalklist)
            serializer.save(user = self.request.user) # --> ㅈㄴ 삽질해서 공부한결과 save를 해야지 값이 들어가는데 문제는 값이 2개가 안들어감 시발 기믹이네-> 됐네 개시발
            #print(Diary.objects.all())
            petwalklist = Diary.objects.filter(Q(user__username = self.request.user) & Q(petwalk__exact = 'o'))# username 과 username이 같은 값 모두 UserPetLis foreign key 접근
            w_num = len(petwalklist)
            serializer.save(petwalknum = w_num)
            #print(w_num)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        '''
        많은 시간을 쏟았는데 안됐던 이유는 우선 foreign key로 값을 접근하는 방법과 perform_create 와 create의 차이를 정확히 알아야 한다.
        foreignkey 같은 경우는 내가 방향성 자체를 조금 잘못 생각했다.
        preform_create 와 create의 차이의 경우 perform_create는 create() 의 동작중 일부분을 overriding한다고 보면된다 -> serializer.save() 될때 호출된다고 생각하는게 맘 편할듯
        그래서 create의 값을들 custom해서 넣고싶을때는 perform_create() 가 아닌 create() 를 해줘야한다.
        '''
    
   # def perform_create(self, serializer):
        
        
        

# @csrf_exempt
# def walking(request):
#      petwalklist = Diary.objects.filter(Q(petwalknum__exact = 1))# username 과 username이 같은 값 모두 UserPetList
#      print(petwalklist)
#      w_num = len(petwalklist)
#      print(w_num)
#      global dic
#      dic = {}
#      return JsonResponse(dic)

        



