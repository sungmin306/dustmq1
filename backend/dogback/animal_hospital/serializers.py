from .models import HospitalDay, HospitalDiary
from rest_framework import serializers

class HospitalDiarySerializer(serializers.ModelSerializer):
    #user = serializers.ReadOnlyField(source = 'user.username') #foreign key user readonly
    class Meta:
        fields = (
            'id',
            'image',
            'hospital_name',
            'title',
            'created_at',
            'required'
        )
        model = HospitalDiary

class HospitalDaySerializer(serializers.ModelSerializer):
    #user = serializers.ReadOnlyField(source = 'user.username') ##foreign key user readonly
    class Meta:
        model = HospitalDay
        fields = (
            'id',
            'hospitalnameing',
            'vaccination',
            'heartworm',
        )
        model = HospitalDay