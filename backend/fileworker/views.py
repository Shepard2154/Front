from rest_framework.response import Response

from student.views import StudentReprViewSet
from .services import get_file

from loguru import logger


class GetFileViewSet(StudentReprViewSet):
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        return get_file('xlsx', queryset)