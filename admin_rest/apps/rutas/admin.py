from django.contrib import admin
from .models import Ciudad, Trayecto


class CiudadAdmin(admin.ModelAdmin):
    # The fields to be used in displaying the User model. These override the definitions on the base UserAdmin that reference specific fields on auth.User.
    list_display = (
        'id',
        'ciudad'
    )
    list_filter = ('ciudad',)
    search_fields = ('ciudad',)
    ordering = ('ciudad',)
    filter_horizontal = ()


class TrayectoAdmin(admin.ModelAdmin):
    # The fields to be used in displaying the User model. These override the definitions on the base UserAdmin that reference specific fields on auth.User.
    list_display = (
        'id',
        'origen',
        'destino'
    )
    fields = ('origen', 'destino')
    list_filter = ('origen', 'destino')
    search_fields = ('origen', 'destino')
    ordering = ('origen', 'destino')
    filter_horizontal = ()


admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(Trayecto, TrayectoAdmin)
