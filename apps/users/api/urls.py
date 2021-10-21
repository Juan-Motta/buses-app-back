from django.urls import path
from .api import user_api_view, user_detail_api_view


urlpatterns = [
    path(
        '',
        user_api_view,
        name='user'
    ),
    path(
        '<str:id>',
        user_detail_api_view,
        name='detailed_user'
    ),
]
