from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.api.urls')),
    path('trayectos/', include('apps.trayectos.api.urls')),
    path('reservas/', include('apps.reservas.api.urls'))

]
