from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DictionaryViewSet, EntryViewSet, LanguagesViewSet, CountryViewSet

router = DefaultRouter()

router.register(r'dictionaries', DictionaryViewSet, basename='dictionary')
router.register(r'entries', EntryViewSet, basename='entry')
router.register(r'languages', LanguagesViewSet, basename='languages')
router.register(r'country', CountryViewSet, basename='country')

urlpatterns = [
    path('', include(router.urls)),
]
