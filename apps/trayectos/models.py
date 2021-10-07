from django.db import models


class Trayecto(models.Model):
    """Representacion del modelo para Trayecto"""
    origen = models.CharField(
        'Origen',
        max_length=30,
        null=False,
        blank=False,
    )
    destino = models.CharField(
        'Destino',
        max_length=30,
        null=False,
        blank=False,
    )
    fecha = models.DateField(
        'Fecha',
        help_text="Escriba la fecha en formato dd/mm/aaaa ejemplo 01/01/2021",
        auto_now=False,
        auto_now_add=False,
        null=False,
        blank=False
    )
    hora = models.TimeField(
        'Hora',
        help_text="Escriba la hora de la forma HH:MM:SS en formato de 24 horas ejemplo 10:00:00",
        auto_now=False,
        auto_now_add=False,
        null=False,
        blank=False
    )
    precio = models.IntegerField(
        'Precio',
        null=False,
        blank=False
    )
    puestos = models.IntegerField(
        'Puestos',
        null=False,
        blank=False
    )

    def save(self, **kwargs):
        self.origen = self.origen.upper()
        self.destino = self.destino.upper()
        super().save(*kwargs)

    class Meta:
        """Definicion de los Metadatos para el modelo de Trayecto"""
        verbose_name = 'Trayecto'
        verbose_name_plural = 'Trayectos'
        ordering = ['fecha', 'hora', 'origen', 'destino']

    def __str__(self):
        """Representacion Unicode del Trayecto"""
        return f'{self.origen} - {self.destino} - {self.fecha} - {self.hora} - {self.precio}'
