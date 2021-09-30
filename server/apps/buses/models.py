from django.db import models


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

    def __str__(self):
        return '{} - {} - {}'.format(self.codigo, self.modelo, str(self.numeroPasajeros))
