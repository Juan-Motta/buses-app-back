from django.contrib import admin
from .models import Persona


class PersonaAdmin(admin.ModelAdmin):
    fields = ('nombres', 'apellidos', 'documento',
              'fecha_nacimiento', 'celular', 'genero')
    list_display = (
        'nombres', 'apellidos', 'documento',
        'fecha_nacimiento', 'celular', 'genero'
    )


admin.site.register(Persona, PersonaAdmin)
