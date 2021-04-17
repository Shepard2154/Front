from rest_framework import serializers

from .models import DirectionModel


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectionModel
        fields = '__all__'