from typing import Any
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from ..models import Dictionary
from ..serializers import DictionarySerializer, EntrySerializer
from rest_framework.permissions import IsAuthenticated, AllowAny


class DictionaryViewSet(viewsets.ModelViewSet):
    queryset = Dictionary.objects.all()
    serializer_class = DictionarySerializer
    permission_classes = [AllowAny]

    @action(detail=True, methods=['get'])
    def entries(self, request: Request, pk: Any = None) -> Response:
        """Get all the entries of a dictionary."""
        dictionary = get_object_or_404(Dictionary, id=pk)
        entries = dictionary.entries.all()
        serializer = EntrySerializer(entries, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
