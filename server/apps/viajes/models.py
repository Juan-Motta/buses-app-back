from django.db import models

from apps.trayectos.models import Trayecto
from apps.buses.models import Bus


class Viaje(models.Model):
    """Modelo para administrar los viajes de la aplicacion"""

    ESTADOS = (
        ('0', 'NO INICIADO'),
        ('1', 'EN TRAYECTO'),
        ('2', 'FINALIZADO'),
        ('3', 'ABORDANDO')
    )

    codigo = models.CharField(
        'Codigo',
        max_length=50,
        null=False,
        blank=False,
        unique=True
    )
    fecha = models.DateField(
        'Fecha',
        auto_now=False,
        null=False,
        blank=False,
        auto_now_add=False
    )
    hora = models.TimeField(
        'Hora',
        auto_now=False,
        auto_now_add=False,
        null=False,
        blank=False
    )
    estado = models.CharField(
        'Estado',
        max_length=1,
        choices=ESTADOS,
        null=False,
        blank=False
    )
    precio = models.IntegerField(
        'Precio',
        null=False,
        blank=False
    )
    trayecto = models.ForeignKey(
        Trayecto,
        on_delete=models.CASCADE
    )
    bus = models.ForeignKey(
        Bus,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return '{} - {} - {} - {}'.format(self.codigo, str(self.fecha), str(self.hora), str(self.trayecto))
