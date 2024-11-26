from typing import Any
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from ..models import Dictionary, Entry
from ..serializers import EntrySerializer


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    permission_classes = [AllowAny]

    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        data = request.data

        try:
            original_name = data['original_name']
            translation = data['translation']
            description = data.get('description', '')
            dictionary_id = data['dictionary_id']

            dictionary = get_object_or_404(Dictionary, id=dictionary_id)

            entry, created = Entry.objects.get_or_create(
                original_name=original_name,
                translation=translation,
                defaults={'description': description}
            )

            entry.dictionaries.add(dictionary)

            message = "Entry created successfully" if created else "Entry already exists, associated with dictionary"
            return Response(
                {'message': message, 'entry': self.get_serializer(entry).data},
                status=status.HTTP_201_CREATED if created else status.HTTP_200_OK
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