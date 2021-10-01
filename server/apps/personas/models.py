from django.db import models
from django.db.models import Max


class Persona(models.Model):

    GENEROS = (
        ('0', 'HOMBRE'),
        ('1', 'MUJER'),
        ('2', 'OTRO')
    )

    nombres = models.CharField(
        'Nombres',
        max_length=50,
        null=False,
        blank=False
    )
    apellidos = models.CharField(
        'Apellidos',
        max_length=50,
        null=False,
        blank=False
    )
    documento = models.CharField(
        'Documento',
        max_length=50,
        null=False,
        blank=False,
        unique=True
    )
    fecha_nacimiento = models.DateField(
        'Fecha nacimiento',
        auto_now=False,
        auto_now_add=False,
        null=False,
        blank=False
    )
    celular = models.CharField(
        'Celular',
        max_length=50,
        null=False,
        blank=False,
    )
    genero = models.CharField(
        'Genero',
        max_length=1,
        choices=GENEROS,
        null=False,
        blank=False
    )

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        ordering = ['apellidos', 'nombres']

    def __str__(self):
        return '{} | {} {} | {}'.format(self.documento, self.nombres, self.apellidos, self.celular)
