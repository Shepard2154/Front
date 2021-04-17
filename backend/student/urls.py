from django.urls import path

from . import views


urlpatterns = [
    path("", views.StudentCreateUpdateViewSet.as_view({'post': 'create'})),
    path("update/<int:pk>/", views.StudentCreateUpdateViewSet.as_view({'put': 'update'})),

    path("all/", views.StudentReprViewSet.as_view({'get': 'list'})),
    path("<int:pk>/", views.StudentReprViewSet.as_view({'get': 'retrieve'})),
]