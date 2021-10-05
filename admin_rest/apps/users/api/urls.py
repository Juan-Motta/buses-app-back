from django.urls import path
from .api import user_api_view, user_detail_api_view


urlpatterns = [
    path(
        'users/',
        user_api_view,
        name='user_api_view'
    ),
    path(
        'users/<str:document>',
        user_detail_api_view,
        name='user_detail_api_view'
    ),
]
