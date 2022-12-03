from rest_framework import serializers
from . models import Diary


class DiarySerializers(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.username')
    #petwalknum = serializers.ReadOnlyField(source = 'petwalknum')
    class Meta:
        fields = ('id','day', 'image', 'context','petwalk','user','petwalknum')
        model = Diary
