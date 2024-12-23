from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from ..serializers import UserStatisticsSerializer


class UserStatisticsViewSet(ViewSet):
    def retrieve(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        serializer = UserStatisticsSerializer(user)
        return Response(serializer.data)
