from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework_simplejwt.views import TokenRefreshView
from apps.users.api.serializers import CustomTokenObtainPairView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('apps.users.api.urls')),
    path('api/trayectos/', include('apps.trayectos.api.urls')),
    path('api/reservas/', include('apps.reservas.api.urls')),
    path('api/token/', CustomTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
