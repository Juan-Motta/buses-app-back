from django.db import models
from apps.users.models import User
from apps.trayectos.models import Trayecto
from django.core.exceptions import ValidationError


class Reserva(models.Model):
    """Representacion del modelo para Reserva"""

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    trayecto = models.ForeignKey(
        Trayecto,
        on_delete=models.CASCADE
    )

    nombre = models.CharField(
        'Nombre',
        max_length=50,
        null=False,
        blank=False
    )

    apellido = models.CharField(
        'Apellido',
        max_length=50,
        null=False,
        blank=False
    )

    documento = models.CharField(
        'Documento',
        max_length=50,
        null=False,
        blank=False
    )
    fecha_nacimiento = models.DateField(
        'Fecha Nacimiento',
        auto_now=False,
        auto_now_add=False,
        null=False,
        blank=False
    )

    telefono = models.CharField(
        'Telefono',
        max_length=10,
        null=False,
        blank=False
    )

    puesto = models.IntegerField(
        'Puesto',
        null=False,
        blank=False
    )

    def clean(self):
        esta_reservado = Reserva.objects.filter(
            puesto=self.puesto,
            trayecto=self.trayecto
        )

        print(self.trayecto.puestos)

        if self.puesto > self.trayecto.puestos and self.puesto < 0:
            raise ValidationError(
                {'puesto': "El puesto seleccionado es invalido"})

        if esta_reservado:
            if esta_reservado[0].id != self.id:
                raise ValidationError(
                    {'puesto': "El puesto ya se encuentra reservado"})

    class Meta:
        """Definicion de los Metadatos para el modelo de Reserva"""
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
        ordering = ['usuario', 'trayecto', 'documento']

    def __str__(self):
        """Representacion Unicode de la Reserva"""
        return f'{self.usuario} - {self.trayecto} - {self.nombre} - {self.apellido} - {self.puesto}'
