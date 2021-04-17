import os

from django.http import HttpResponse
from wsgiref.util import FileWrapper

from django_pandas.io import read_frame

from config import settings


def get_file(file_format: str, data) -> HttpResponse:
    filename = str(settings.BASE_DIR) + f'/media/data.{file_format}'
    read_frame(data).to_excel(filename)

    with open(filename, 'rb') as short_report:
        # конструирование ответа
        content = f'application/{file_format}'
        response = HttpResponse(
                FileWrapper(short_report),
                content_type=content
            )
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        os.remove(filename) # удаление файла
        return response