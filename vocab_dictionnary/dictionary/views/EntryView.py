from typing import Any
from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from ..models import Dictionary, Entry, Description
from ..serializers import EntrySerializer
from django.contrib.auth.models import User



class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    permission_classes = [AllowAny]

    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        data = request.data

        try:
            original_name = data['original_name']
            translation = data['translation']
            description_text = data.get('description', '')
            dictionary_id = data['dictionary_id']

            dictionary = get_object_or_404(Dictionary, id=dictionary_id)

            entry, created = Entry.objects.get_or_create(
                original_name=original_name,
                translation=translation,
            )

            existing_description = Description.objects.filter(
                entry=entry,
                created_by=request.user
            ).first()

            if not existing_description:
                Description.objects.create(
                    entry=entry,
                    text=description_text,
                    created_by=request.user
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
        
    @action(detail=False, methods=['get'], url_path='recent_activity')
    def recent_activity(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        user = self.request.user

        if not user.is_authenticated:
            return Response(
                {"error": "User is not authenticated"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        dictionaries = Dictionary.objects.filter(user=user)

        recent_entries = Entry.objects.filter(
            dictionaries__in=dictionaries
        ).distinct().order_by('-created_at')[:10]

        serializer = self.get_serializer(recent_entries, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)