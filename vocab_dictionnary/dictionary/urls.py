from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.DictionaryView import DictionaryViewSet
from .views.EntryView import EntryViewSet

router = DefaultRouter()

router.register(r'dictionaries', DictionaryViewSet, basename='dictionary')
router.register(r'entries', EntryViewSet, basename='entry')

urlpatterns = [
    path('', include(router.urls)),
]
