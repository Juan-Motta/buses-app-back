from django.db import models
from django.db.models import Max


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

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
        ordering = ['ciudad', ]

    def __str__(self):
        return '{} {}'.format(self.abreviacion, self.ciudad)


class Trayecto(models.Model):
    """Clase para administrar los trayectos"""

    codigo = models.CharField(
        'Codigo',
        max_length=50,
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

    def save(self, **kwargs):
        if not self.codigo:
            max = Trayecto.objects.aggregate(id_max=Max('id'))['id_max']
            self.codigo = "{}{}{:03d}".format(
                str(self.origen)[0:3],
                str(self.destino)[0:3],
                max if max is not None else 1)
        super().save(*kwargs)

    class Meta:
        verbose_name = 'Trayecto'
        verbose_name_plural = 'Trayectos'
        ordering = ['codigo', 'origen', 'destino']

    def __str__(self):
        return '{} --> {}'.format(str(self.origen), str(self.destino))
