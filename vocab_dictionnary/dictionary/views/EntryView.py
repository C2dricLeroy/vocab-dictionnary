from typing import Any
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from ..models import Dictionary, Entry
from ..serializers import EntrySerializer

class EntryViewSet(viewsets.ModelViewSet):
    queryset = Dictionary.objects.all()
    serializer_class = EntrySerializer
    permission_classes = [IsAuthenticated]
    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        data = request.data
        try:
            name = data['name']
            traduction = data['traduction']
            dictionary_id = data['dictionary_id']
            dictionary = get_object_or_404(Dictionary, id=dictionary_id)
            entry = Entry(
                name=name,
                traduction=traduction,
                dictionary=dictionary
            )
            entry.save()
            return Response(
                {'message': 'Entry created successfully'},
                status=status.HTTP_201_CREATED
            )
        except KeyError as e:
            return Response(
                {'error': f"Missing key: {e.args[0]}"},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @action(detail=True, methods=['get'])
    def get_entry(self, request: Request, pk: Any = None) -> Response:
        entry_id = request.GET.get('id')

        if not entry_id:
            return Response(
                {"error": "Missing 'id' parameter"},
                status=status.HTTP_400_BAD_REQUEST
            )
        entry: Entry = get_object_or_404(Entry, id=entry_id)
        serializer: EntrySerializer = self.get_serializer(entry)
        return Response(serializer.data)
