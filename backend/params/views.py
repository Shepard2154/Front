from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from . import consts
from .models import DirectionModel
from .serializers import DirectionSerializer
from .filters import DirectionFilter


class GetRegions(APIView):
    def get(self, request, *args, **kwargs):
        return Response(consts.TOMSK_REGIONS, status=200)


class DirectionViewSet(viewsets.ModelViewSet):
    queryset = DirectionModel.objects.all()
    serializer_class = DirectionSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = DirectionFilter