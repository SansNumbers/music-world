from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from apps.user.api.views import MyProfileRetrieveUpdateAPIView, RegisterUserAPIView

urlpatterns = [
    path('users/', RegisterUserAPIView.as_view(), name='register'),
    path('auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me/', MyProfileRetrieveUpdateAPIView.as_view(), name='my_profile'),
]
