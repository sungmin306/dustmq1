from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Diary(models.Model): # Diary
    WALKING_CHOICE = (
        ('o','1'),
        ('x','0')
    )
    id = models.AutoField(primary_key=True, null=False, blank=False) #pk
    day = models.DateField() # 기록날짜
    image = models.ImageField(null=True, blank= True) #사진
    context = models.TextField(max_length = 500) # 일기 내용
    pet_walk = models.CharField(max_length=1,choices=WALKING_CHOICE)
    #user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE, default = '') # user foreign key