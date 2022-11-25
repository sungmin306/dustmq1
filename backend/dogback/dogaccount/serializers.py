from rest_framework import serializers
from .models import DogAccount#, DogWeight
class Dog_accountSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'petname',
            'petyear',
            'petspecies',
            'petweight',
            'petpublicnum',
            'petsex',
            'petdesex',
            'petimage',
            'noseprint',

        )
        model = DogAccount

# class DogWeightSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = (
#             'pet_weight_days', 'pet_weight'
#         )
#         model = DogWeight



# class PetImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = (
#             'pet_image',
#             'nose_vec'
#         )
#         model = DogAccount

# class Nose_vectorSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = (
#             'image',
#             'nose_vec',

#         )
#         moel = Nose_vector
# #  id = models.AutoField(primary_key=True, null=False, blank=False) # PK 자동생성
#     pet_name = models.CharField(max_length = 10)
#     pet_year = models.DateField(null=False, blank=False, max_lengh=10)
#     pet_species = models.CharField(null=False, blank=False, max_length=20)
#     pet_weight = models.FloatField(null = False, blank = False)
#     pet_publicnum = models.IntegerField(null = True, blank = True)
#     pet_sex = models.CharField(max_length=1, choices = PET_SEX_CHOICE) 
#     pet_desex = models.CharField(max_length=1, choices = PET_DESEX_CHOICE)
#     nose_print = models.ForeignKey(Nose_vector, null=False, blank = False, on_delete = models.CASCADE, default = '') # 비분 벡터값
#     user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE, default = '')