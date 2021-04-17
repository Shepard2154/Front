from rest_framework.permissions import BasePermission

from django.contrib.auth.models import Group


class IsManager(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and _is_in_group(request.user, 'manager'))


class IsTeacher(BasePermission):
    
    def has_permission(self, request, view):
        return bool(request.user and _is_in_group(request.user, 'teacher'))


class IsStudent(BasePermission):
    
    def has_permission(self, request, view):
        return bool(request.user and _is_in_group(request.user, 'student'))


def _is_in_group(user, group_name):
    """ Принимает пользователя и название группы, возращает True, если пользователь в группе """
    try:
        return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()
    except Group.DoesNotExist:
        return None