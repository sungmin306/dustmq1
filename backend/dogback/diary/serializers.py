from rest_framework import serializers
from . models import Diary


class DiarySerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('day', 'image', 'context','pet_walk','pet_walk_num')
        model = Diary
