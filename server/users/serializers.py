from rest_framework import serializers

from .models import Tokenstable, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
        ]


class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password'
        ]


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tokenstable
        fields = [
            'userid',
            'resetToken',
        ]
