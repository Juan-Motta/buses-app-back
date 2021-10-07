from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/', include('apps.users.api.urls')),
    path('trayecto/', include('apps.trayectos.api.urls')),
    path('reserva/', include('apps.reservas.api.urls'))
]
