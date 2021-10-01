from django.contrib import admin
from .models import Bus


class BusAdmin(admin.ModelAdmin):
    fields = ('modelo', 'numeroPasajeros', 'wc', 'wifi', 'aireAcondicionado')
    list_display = (
        'codigo',
        'modelo',
        'numeroPasajeros',
        'wc',
        'wifi',
        'aireAcondicionado'
    )


admin.site.register(Bus, BusAdmin)
