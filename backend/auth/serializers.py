from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User, Group
from django.core import exceptions as django_exceptions
from django.db import transaction

from djoser.serializers import UserCreateSerializer
from djoser.conf import settings

from rest_framework.exceptions import ValidationError
from rest_framework.settings import api_settings
from rest_framework import serializers


class GroupField(serializers.CharField):
    def to_representation(self, value):
        return [i.name for i in value.all()]

    def to_internal_value(self, data):
        return Group.objects.get(name=data)


class MyUserSerializer(UserCreateSerializer):
    groups = GroupField(required=False, default = Group.objects.get(name='student'))
    password = serializers.CharField(write_only=True)
    email = serializers.CharField()

    def validate(self, attrs):
        attrs = dict(attrs)
        group = attrs.pop('groups')
        user = User(**attrs)        
        password = attrs.get("password")
        try:
            validate_password(password, user)
        except django_exceptions.ValidationError as e:
            serializer_error = serializers.as_serializer_error(e)
            raise serializers.ValidationError(
                {"password": serializer_error[api_settings.NON_FIELD_ERRORS_KEY]}
            )
        attrs['groups'] = group
        return attrs

    def perform_create(self, validated_data):
        group = validated_data.pop('groups')
        with transaction.atomic():
            user = User.objects.create_user(**validated_data)
            user.groups.add(group)
        return user

    class Meta:
        model = User
        fields = ['username', 'groups', 'password', 'email']


class MyTokenSerializer(serializers.ModelSerializer):
    auth_token = serializers.CharField(source="key")
    user_group = serializers.SerializerMethodField('get_group')

    def get_group(self, obj):
        return obj.user.groups.values_list('name', flat=True).first()

    class Meta:
        model = settings.TOKEN_MODEL
        fields = ("auth_token", "user_group")