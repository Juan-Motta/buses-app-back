from django.db import models
from django.db.models import Max


class Bus(models.Model):
    """Clase para administrar los buses"""
    codigo = models.CharField(
        'Codigo',
        unique=True,
        null=False,
        blank=False,
        max_length=50,
    )
    modelo = models.CharField(
        'Modelo',
        null=False,
        blank=False,
        max_length=50
    )
    numeroPasajeros = models.IntegerField(
        'Numero de pasajeros',
        blank=False,
        null=False
    )
    wc = models.BooleanField(
        'Tiene Baño',
        null=False,
        blank=False,
        default=False
    )
    wifi = models.BooleanField(
        'Tiene Wi-Fi',
        null=False,
        blank=False,
        default=False
    )
    aireAcondicionado = models.BooleanField(
        'Tiene Aire Acondicionado',
        null=False,
        blank=False,
        default=False
    )

    def save(self, **kwargs):
        if not self.codigo:
            max = Bus.objects.aggregate(id_max=Max('id'))['id_max']
            self.codigo = "{}{:03d}".format(
                'B',
                max if max is not None else 1)
        super().save(*kwargs)

    class Meta:
        verbose_name = 'Bus'
        verbose_name_plural = 'Buses'
        ordering = ['codigo']

    def __str__(self):
        return '{}'.format(self.modelo)
