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
