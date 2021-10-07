from django.urls import path
from .api import trayecto_api_view, trayecto_detail_api_view


urlpatterns = [
    path(
        '',
        trayecto_api_view,
        name='trayecto'
    ),
    path(
        '<int:id>',
        trayecto_detail_api_view,
        name='detailed_trayecto'
    )
]
