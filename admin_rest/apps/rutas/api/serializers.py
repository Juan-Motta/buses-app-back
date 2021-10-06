from django.db import models
from django.db.models import fields
from rest_framework import serializers
from apps.rutas.models import Ciudad
from apps.rutas.models import Trayecto


class CiudadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ciudad
        fields = '__all__'


class TrayectoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trayecto
        fields = '__all__'


class TrayectoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trayecto
        exclude = ['id']
