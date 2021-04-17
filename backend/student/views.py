from datetime import datetime

from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import DurationField
from django.db.models import F

from .models import StudentModel
from .serializers import StudentSerializer, StudentReprSerializer
from .filters import StudentFilter


class StudentCreateUpdateViewSet(viewsets.ModelViewSet):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer


class StudentReprViewSet(viewsets.ModelViewSet):
    queryset = StudentModel.objects.all()\
    .annotate(current_curse = datetime.now().date() - F('receipt_date'))

    serializer_class = StudentReprSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = StudentFilter