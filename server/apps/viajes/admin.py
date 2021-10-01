from django.contrib import admin
from .models import Viaje


class ViajeAdmin(admin.ModelAdmin):
    list_filter = ('estado', 'trayecto')
    fields = ('fecha', 'hora', 'estado', 'precio', 'trayecto', 'bus')
    list_display = (
        'codigo',
        'fecha',
        'hora',
        'estado',
        'precio',
        'trayecto',
        'bus'
    )


admin.site.register(Viaje, ViajeAdmin)
