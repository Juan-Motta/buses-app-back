from rest_framework import serializers
from apps.trayectos.models import Trayecto


class TrayectoListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trayecto
        fields = [
            'id',
            'origen',
            'destino',
            'fecha',
            'hora',
            'precio',
            'puestos',
        ]


class TrayectoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trayecto
        fields = [
            'origen',
            'destino',
            'fecha',
            'hora',
            'precio',
            'puestos',
        ]

    def create(self, validated_data):
        trayecto = Trayecto(**validated_data)
        trayecto.save()
        return trayecto

    def update(self, instance, validated_data):
        updated_trayecto = super().update(instance, validated_data)
        updated_trayecto.save()
        return updated_trayecto
