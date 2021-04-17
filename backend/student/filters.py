from django.db.models import Q
from django_filters import rest_framework as filters

from params.models import DirectionModel
from .models import StudentModel


class StudentFilter(filters.FilterSet):
    birthdate = filters.DateFromToRangeFilter()
    att_score = filters.NumericRangeFilter(lookup_expr='range')
    examins_score = filters.NumericRangeFilter(lookup_expr='range')

    spec_name = filters.CharFilter(method='filter_direction')
    colledge_name = filters.CharFilter(method='filter_colledge')
    prof_name = filters.CharFilter(method='filter_prof')

    def filter_direction(self, queryset, name, values):
        fil = Q()
        for value in values.split(','):
            for direction in DirectionModel.objects.filter(spec_name=value.strip()):
                fil |= Q(direction=direction)
        return queryset.filter(fil)

    def filter_colledge(self, queryset, name, values):
        fil = Q()
        for value in values.split(','):
            for direction in DirectionModel.objects.filter(colledge_name=value.strip()):
                fil |= Q(direction=direction)
        return queryset.filter(fil)

    def filter_prof(self, queryset, name, values):
        fil = Q()
        for value in values.split(','):
            for direction in DirectionModel.objects.filter(prof_name=value.strip()):
                fil |= Q(direction=direction)
        return queryset.filter(fil)

    o = filters.OrderingFilter(fields=(
            ('birthdate', 'birthdate'),
            ('att_score', 'att_score'),
            ('receipt_date', 'receipt_date'),
            ('current_curse', 'current_curse'),
        ))

    class Meta:
        model = StudentModel
        fields = ['birthdate', 'att_score', 'examins_score', 'is_disabled',
                  'is_orphan', 'is_served', 'needs_home', 'region',
                  'male', 'spec_name', 'colledge_name', 'prof_name']