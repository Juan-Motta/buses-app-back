from rest_framework import serializers
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

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


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

    def to_representation(self, instance):
        return {
            # 'id': instance['id'],
            'password': instance['password'],
            'email': instance['email'],
            'name': instance['name'],
            'last_name': instance['last_name'],
            'image': instance['image'],
            'document': instance['document'],
            'birth': instance['birth'],
            'phone': instance['phone'],
            'is_active': instance['is_active'],
            'is_staff': instance['is_staff']
        }
