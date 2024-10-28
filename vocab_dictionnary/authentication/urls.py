from rest_framework.routers import DefaultRouter
from .views import UserViewSet, LexiLearnTokenObtainPairView
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'register', UserViewSet, basename='user')

urlpatterns = [
    path('login/', LexiLearnTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me/', UserViewSet.as_view({'get': 'me'}), name='me'),
]

urlpatterns += router.urls
