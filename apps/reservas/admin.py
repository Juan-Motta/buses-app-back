from django.contrib import admin
from .models import Reserva


class ReservaAdmin(admin.ModelAdmin):
    fields = ('usuario', 'trayecto', 'nombre', 'apellido',
              'documento', 'fecha_nacimiento', 'telefono', 'puesto')
    list_display = (
        'id',
        'usuario',
        'trayecto',
        'nombre',
        'apellido',
        'documento',
        'fecha_nacimiento',
        'telefono',
        'puesto'
    )
    search_fields = ('nombre', 'apellido')


admin.site.register(Reserva, ReservaAdmin)
