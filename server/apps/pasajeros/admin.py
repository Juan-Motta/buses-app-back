from django.contrib import admin
from .models import Pasajero


class PasajeroAdmin(admin.ModelAdmin):
    fields = ('viaje', 'persona', 'asiento')
    list_display = (
        'codigo',
        'viaje',
        'persona',
        'asiento',
    )


admin.site.register(Pasajero, PasajeroAdmin)
