from datetime import datetime

from rest_framework import serializers

from params.serializers import DirectionSerializer
from .models import StudentModel

from django.db.models.functions import TruncMonth, Lag
from django.db.models import Sum, F, Window
from loguru import logger


class StudentSerializer(serializers.ModelSerializer):
    user_model = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = StudentModel
        fields = '__all__'

class StudentReprSerializer(StudentSerializer):
    direction = DirectionSerializer()
    current_curse = serializers.SerializerMethodField(read_only=True)
    study_end = serializers.SerializerMethodField(read_only=True)

    def get_current_curse(self, obj):
        return (obj.current_curse - obj.academ_duration.days)//356 

    def get_study_end(self, obj):
        if obj.is_higher: duration = obj.direction.base_study_time
        else: duration = obj.direction.short_study_time
        return obj.receipt_date + duration + obj.academ_duration