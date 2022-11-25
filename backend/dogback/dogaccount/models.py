from django.db import models
from django.contrib.auth.models import User
# Create your models here.

'''
delete migration
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
'''

#이미지 저장하는 table -> 추후 media 로 파일 전송
# class Pet_img():
#     image = models.ImageField()

# img 모델을 처리하고 이미지를 가지고 비문추출 작업을 진행 그리고 그 값을 다시 Nose_vector 값에 저장하고 그 값을 FOREIGN key로 활용

# class Nose_vector(models.Model):
#     #nose_img = models.ImageField(primary_key = True)
#     image = models.ImageField()
#     nose_vec= models.IntegerField(null=True, blank=True) # 나중에 unique key 로 변환 



#nose_print = models.ForeignKey(Nose_vector, null=False, blank = False, on_delete = models.CASCADE, default = '', related_name='select_print') # 비분 벡터값
class DogAccount(models.Model):
    PET_SEX_CHOICE = (
        ('M','male'),
        ('F','female')
    )
    PET_DESEX_CHOICE=(
        ('O', '1'), #neutrality
        ('X', '0') #no_neutrality
    )
    PET_NOSE_PRINT = (
        ('O','1'),
        ('X','0')
    )
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE, default = '') # user foreign key
    id = models.AutoField(primary_key=True, null=False, blank=False) # PK 자동생성
    petname = models.CharField(null = True , blank = True ,max_length = 10) # 이름
    petyear = models.DateField(null=True, blank=True) # 생년월일
    petspecies = models.CharField(null=True, blank=True, max_length=20) # 종
    petweight = models.FloatField(null = True, blank = True) # 무게
    petpublicnum = models.IntegerField(null = True, blank = True) # 등록번호
    petsex = models.CharField(null = True , blank = True , max_length=1, choices = PET_SEX_CHOICE) # 성별
    petdesex = models.CharField(null = True , blank = True, max_length=1, choices = PET_DESEX_CHOICE) # 중성화여부
    petimage = models.ImageField(null=True, blank = True) # 사진
    noseprint = models.CharField(null=True, blank = True, max_length=1, choices = PET_NOSE_PRINT )#비문 등록 추가 여부
    noseimage = models.ImageField(null = True, blank = True) #비문 사진
# class DgoNoseImage(models.Model):
#     dogprofile = models.ForeignKey(DogAccount, on_delete=models.CASCADE, default='', related_name = 'weights')
#     noseimage = models.ImageField()
