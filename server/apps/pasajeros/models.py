from django.db import models
from django.db.models import Max

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

    def save(self, **kwargs):
        if not self.codigo:
            max = Pasajero.objects.aggregate(id_max=Max('id'))['id_max']
            self.codigo = "{}{:03d}".format(
                'P',
                max if max is not None else 1)
        super().save(*kwargs)

    class Meta:
        verbose_name = 'Pasajero'
        verbose_name_plural = 'Pasajeros'
        ordering = ['persona']

    def __str__(self):
        return '{} - {} - {}'.format(str(self.persona), str(self.viaje), str(self.asiento))
