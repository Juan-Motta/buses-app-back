from rest_framework import serializers
from apps.users.models import User


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'name',
            'last_name',
            'document',
            'birth',
            'phone',
            'is_active',
            'is_staff'
        ]


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username',
            'name',
            'last_name',
            'email',
            'password',
            'document',
            'birth',
            'phone',
        ]

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        updated_user = super().update(instance, validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user
