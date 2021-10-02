from django.urls import path
from apps.users.api.api import UserAPIView

urlpatterns = [
    path('get-users/', UserAPIView.as_view(), name='user_api')
]
