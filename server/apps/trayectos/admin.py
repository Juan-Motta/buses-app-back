from django.contrib import admin
from .models import Ciudad
from .models import Trayecto


class CiudadAdmin(admin.ModelAdmin):
    list_display = (
        'abreviacion',
        'ciudad'
    )


class TrayectoAdmin(admin.ModelAdmin):
    list_filter = ('origen', 'destino')
    fields = ('origen', 'destino')
    list_display = (
        'codigo',
        'origen',
        'destino'
    )


admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(Trayecto, TrayectoAdmin)
