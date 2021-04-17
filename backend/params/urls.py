from django.urls import path

from . import views


urlpatterns = [
    path('regions/', views.GetRegions.as_view()),
    path("direction/", views.DirectionViewSet.as_view({'get': 'list'})),
    path("direction/<int:pk>/", views.DirectionViewSet.as_view({'get': 'retrieve'})),
]