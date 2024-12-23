from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GlobalStatisticsViewSet, UserStatisticsViewSet

router = DefaultRouter()

router.register(r'', GlobalStatisticsViewSet, basename='global')
router.register(r'user', UserStatisticsViewSet, basename='user')


urlpatterns = [
    path('', include(router.urls)),
]
