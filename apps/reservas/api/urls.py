from django.urls import path
from .api import reserva_api_view, reserva_detail_api_view


urlpatterns = [
    path(
        '',
        reserva_api_view,
        name='reserva'
    ),
    path(
        '<int:id>',
        reserva_detail_api_view,
        name='detailed_reserva'
    ),
]
