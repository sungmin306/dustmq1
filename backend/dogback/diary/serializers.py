from rest_framework import serializers
from . models import Diary


class DiarySerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('id','day', 'image', 'context','pet_walk')
        model = Diary
