from django.db import models


class Ciudad(models.Model):
    """Clase para administrar las ciudades """
    ciudad = models.CharField(
        'Ciudad',
        max_length=50,
        blank=False,
        null=False,
        unique=True
    )
    abreviacion = models.CharField(
        'Abreviacion',
        max_length=5,
        blank=False,
        null=False,
        unique=True
    )

    def __str__(self):
        return '{} - {}'.format(self.ciudad, self.abreviacion)


class Trayecto(models.Model):
    """Clase para administrar los trayectos"""

    codigo = models.CharField(
        'Codigo',
        max_length=50,
        blank=False,
        null=False,
        unique=True
    )
    origen = models.ForeignKey(
        Ciudad,
        on_delete=models.CASCADE,
        related_name="origen"
    )
    destino = models.ForeignKey(
        Ciudad,
        on_delete=models.CASCADE,
        related_name="destino"
    )

    def __str__(self):
        return '{} - {} - {}'.format(self.codigo, str(self.origen), str(self.destino))
