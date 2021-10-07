from rest_framework import serializers, validators
from apps.reservas.models import Reserva

from apps.users.api.serializers import UserListSerializer
from apps.trayectos.api.serializers import TrayectoListSerializer


class ReservaListSerializer(serializers.ModelSerializer):

    usuario = UserListSerializer()
    trayecto = TrayectoListSerializer()

    class Meta:
        model = Reserva
        fields = '__all__'


class ReservaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reserva
        fields = '__all__'

    def validate(self, data):

        if data['puesto'] > data['trayecto'].puestos or data['puesto'] < 0:
            raise serializers.ValidationError(
                {'message': 'El puesto seleccionado es invalido.'}
            )
        return data

    def create(self, validated_data):
        reserva = Reserva(**validated_data)

        esta_reservado = Reserva.objects.filter(
            puesto=reserva.puesto,
            trayecto=reserva.trayecto.id
        )

        if esta_reservado:
            raise serializers.ValidationError(
                {'message': 'El puesto ya se encuentra reservado'}
            )

        reserva.save()
        return reserva

    def update(self, instance, validated_data):
        updated_reserva = super().update(instance, validated_data)

        esta_reservado = Reserva.objects.filter(
            puesto=updated_reserva.puesto,
            trayecto=updated_reserva.trayecto.id
        )

        if esta_reservado:
            if esta_reservado[0].id != updated_reserva.id:
                raise serializers.ValidationError(
                    {'message': 'El puesto ya se encuentra reservado'}
                )

        updated_reserva.save()
        return updated_reserva
