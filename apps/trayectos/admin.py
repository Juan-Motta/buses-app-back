from django.contrib import admin
from .models import Trayecto


class TrayectoAdmin(admin.ModelAdmin):
    list_filter = ('origen', 'destino')
    fields = ('origen', 'destino', 'fecha', 'hora', 'precio', 'puestos')
    list_display = (
        'origen',
        'destino',
        'fecha',
        'hora',
        'precio',
        'puestos'
    )
    search_fields = ('origen', 'destino')


admin.site.register(Trayecto, TrayectoAdmin)
