from django.db import models

from apps.personas.models import Persona
from apps.viajes.models import Viaje


class Pasajero(models.Model):
    """Clase para administrar los pasajeros"""
    codigo = models.CharField(
        'Codigo',
        max_length=50,
        unique=True,
        null=False,
        blank=False
    )
    viaje = models.ForeignKey(Viaje, on_delete=models.CASCADE)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    asiento = models.IntegerField(
        'Asiento',
        null=False,
        blank=False,
        unique=True
    )

    def __str__(self):
        return '{} - {} - {}'.format(str(self.persona), str(self.viaje), str(self.asiento))
