from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import Languages
from ..serializers import LanguagesSerializers

class LanguagesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Languages.objects.all()
    serializer_class = LanguagesSerializers
    # permission_classes = [IsAuthenticated]
