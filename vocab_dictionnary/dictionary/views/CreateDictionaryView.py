from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models import Dictionnary, Languages, Entry
import json

from ..serializers.DictionarySerializer import DictionarySerializer


class CreateDictionaryView(APIView):
    def post(self, request):
        serializer = DictionarySerializer(data=request.data)
        if serializer.is_valid():
            source_language = get_object_or_404(
                Languages, id=serializer.validated_data['source_language']
            )
            target_language = get_object_or_404(
                Languages, id=serializer.validated_data['target_language']
            )
            Dictionnary.objects.create(
                name=serializer.validated_data['name'],
                source_language=source_language,
                target_language=target_language
            )
            return Response(
                {'message': 'Dictionary created successfully'},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
