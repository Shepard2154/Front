from django.urls import path

from . import views


urlpatterns = [
    path("", views.GetFileViewSet.as_view({'get': 'list'})),
]