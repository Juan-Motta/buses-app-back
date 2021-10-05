from django.db import models
from simple_history.models import HistoricalRecords


class Ciudad(models.Model):
    """Definicion de modelo para ciudades"""
    id = models.CharField(
        'id',
        max_length=5,
        blank=False,
        null=False,
        unique=True,
        primary_key=True
    )
    ciudad = models.CharField(
        'Ciudad',
        max_length=50,
        blank=False,
        null=False,
        unique=True
    )
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
        ordering = ['ciudad']

    def __str__(self):
        return f'{self.id} {self.ciudad}'


class Trayecto(models.Model):
    """Definicion de modelo para trayectos"""

    id = models.CharField(
        'id',
        max_length=50,
        unique=True,
        primary_key=True
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
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def save(self, **kwargs):
        if not self.id:
            self.id = f'{str(self.origen)[0:3]}{str(self.destino)[0:3]}'
        super().save(*kwargs)

    class Meta:
        verbose_name = 'Trayecto'
        verbose_name_plural = 'Trayectos'
        ordering = ['id', 'origen', 'destino']

    def __str__(self):
        return f'{str(self.origen)} --> {str(self.destino)}'
