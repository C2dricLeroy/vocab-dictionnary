from typing import Any
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from ..models import Dictionary, Languages
from ..serializers import DictionarySerializer
from rest_framework.permissions import IsAuthenticated, AllowAny


class DictionaryViewSet(viewsets.ModelViewSet):
    queryset = Dictionary.objects.all()
    serializer_class = DictionarySerializer
    permission_classes = [AllowAny]

    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """
        Custom create method to handle creation of a Dictionary instance.
        """
        serializer: DictionarySerializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            source_language: Languages = get_object_or_404(
                Languages, id=serializer.validated_data['source_language']
            )
            target_language: Languages = get_object_or_404(
                Languages, id=serializer.validated_data['target_language']
            )
            Dictionary.objects.create(
                name=serializer.validated_data['name'],
                source_language=source_language,
                target_language=target_language
            )
            return Response(
                {'message': 'Dictionary created successfully'},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @action(detail=True, methods=['get'])
    # def get_dictionary(self, request: Request, pk: Any = None) -> Response:
    #     """
    #     Custom action to get a dictionary by its ID.
    #     """
    #     dictionary: Dictionary = self.get_object()
    #     serializer: DictionarySerializer = self.get_serializer(dictionary)
    #     return Response(serializer.data)
