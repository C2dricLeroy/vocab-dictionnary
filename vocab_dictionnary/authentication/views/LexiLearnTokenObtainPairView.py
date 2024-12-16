from rest_framework_simplejwt.views import TokenObtainPairView
from ..serializers import (LexiLearnTokenObtainPairSerializer)
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from datetime import timedelta


class LexiLearnTokenObtainPairView(TokenObtainPairView):
    serializer_class = LexiLearnTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        tokens = serializer.validated_data

        user_id = tokens.get("user_id")

        response_data = {
            "user_id": user_id,
        }

        response = Response(response_data, status=status.HTTP_200_OK)

        response.set_cookie(
            key='access_token',
            value=tokens['access'],
            httponly=True,
            secure=True,
            samesite='Lax',
            expires=timezone.now() + timedelta(days=1)
        )

        response.set_cookie(
            key='refresh_token',
            value=tokens['refresh'],
            httponly=True,
            secure=True,
            samesite='Lax',
            expires=timezone.now() + timedelta(days=7)
        )

        return response
