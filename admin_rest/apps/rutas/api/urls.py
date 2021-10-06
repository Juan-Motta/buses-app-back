from django.urls import path
from .api import (
    get_ciudad_api_view,
    get_ciudad_by_id_api_view,
    get_trayecto_api_view,
    get_trayecto_by_id_api_view,
    post_ciudad_api_view,
    post_trayecto_api_view
)

urlpatterns = [
    path(
        'get-ciudades/',
        get_ciudad_api_view,
        name='Get Ciudad Api View'
    ),
    path(
        'get-ciudad/<str:pk>',
        get_ciudad_by_id_api_view,
        name='Get Ciudad Api View'
    ),
    path(
        'get-trayectos/',
        get_trayecto_api_view,
        name='Get Trayecto Api View'
    ),
    path(
        'get-trayecto/<str:pk>',
        get_trayecto_by_id_api_view,
        name='Get Trayecto Api View'
    ),
    path(
        'post-ciudad/',
        post_ciudad_api_view,
        name='Post Ciudad Api View'
    ),
    path(
        'post-trayecto/',
        post_trayecto_api_view,
        name='Post Trayecto Api View'
    )
]
