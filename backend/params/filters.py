from django_filters import rest_framework as filters

from .models import DirectionModel


class DirectionFilter(filters.FilterSet):
    class Meta:
        model = DirectionModel
        fields = ['colledge_name', 'spec_name', 'prof_name']